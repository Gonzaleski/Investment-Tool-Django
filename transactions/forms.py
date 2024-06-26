from django import forms
from .models import Transaction
from share.models import Share, DailyPrice
from jalali_date.fields import JalaliDateField
from django.core.exceptions import ValidationError

class TransactionFilterForm(forms.Form):
    TRANSACTION_TYPES = [
        ('', 'All'),
        (Transaction.BUY, 'Buy'),
        (Transaction.SELL, 'Sell'),
    ]
    
    type        = forms.ChoiceField(choices=TRANSACTION_TYPES, required=False)
    portfo      = forms.CharField(max_length=100, required=False)
    date_from   = forms.DateField(required=False, widget=forms.TextInput(attrs={'data-jdp' : ""}))
    date_to     = forms.DateField(required=False, widget=forms.TextInput(attrs={'data-jdp' : ""}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class TransactionForm(forms.ModelForm):
    symbol = forms.CharField(widget=forms.TextInput(attrs={'id': 'share-autocomplete'}))
    gold_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    dollar_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    class Meta:
        model = Transaction
        fields = ['symbol', 'type', 'portfo', 'date', 'price', 'quantity', 'gold_price', 'dollar_price']

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('date'))  # date format is "yyyy-mm-dd"

        if self.instance and self.instance.pk:
            self.fields['symbol'].initial = self.instance.share.symbol
            self.fields['gold_price'].initial = self.instance.daily_price.gold_price if self.instance.daily_price else None
            self.fields['dollar_price'].initial = self.instance.daily_price.dollar_price if self.instance.daily_price else None

        for field_name, field in self.fields.items():
            if field_name == "date":
                field.widget.attrs.update({'class': 'form-control', 'data-jdp': ""})
            else:
                field.widget.attrs.update({'class': 'form-control'})

    def clean_symbol(self):
        symbol = self.cleaned_data.get('symbol')
        if not Share.objects.filter(symbol=symbol).exists():
            raise ValidationError('The specified share symbol does not exist.')
        return symbol

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise ValidationError('Quantity must be greater than zero.')
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError('Price must be greater than zero.')
        return price

    def clean_gold_price(self):
        gold_price = self.cleaned_data.get('gold_price')
        if gold_price is not None and gold_price <= 0:
            raise ValidationError('Gold price must be greater than zero.')
        return gold_price

    def clean_dollar_price(self):
        dollar_price = self.cleaned_data.get('dollar_price')
        if dollar_price is not None and dollar_price <= 0:
            raise ValidationError('Dollar price must be greater than zero.')
        return dollar_price

    def save(self, commit=True):
        instance = super(TransactionForm, self).save(commit=False)
        symbol = self.cleaned_data.get('symbol')
        gold_price = self.cleaned_data.get('gold_price')
        dollar_price = self.cleaned_data.get('dollar_price')
        
        if symbol:
            instance.share, created = Share.objects.get_or_create(symbol=symbol)
        
        if commit:
            # Ensure that the daily_price is correctly set and updated
            if not instance.daily_price:
                instance.daily_price, created = DailyPrice.objects.get_or_create(
                    user=instance.user, 
                    date=instance.date,
                    defaults={'gold_price': gold_price or 0, 'dollar_price': dollar_price or 0}
                )
            else:
                instance.daily_price.gold_price = gold_price
                instance.daily_price.dollar_price = dollar_price
                instance.daily_price.save()

            instance.save()
        return instance