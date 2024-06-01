from django import forms
from .models import Transaction
from share.models import Share

class TransactionFilterForm(forms.Form):
    TRANSACTION_TYPES = [
        ('', 'All'),
        (Transaction.BUY, 'Buy'),
        (Transaction.SELL, 'Sell'),
    ]
    
    type        = forms.ChoiceField(choices=TRANSACTION_TYPES, required=False)
    portfo      = forms.CharField(max_length=100, required=False)
    date_from   = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    date_to     = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class TransactionForm(forms.ModelForm):
    share = forms.CharField(widget=forms.TextInput(attrs={'id': 'share-autocomplete'}))

    class Meta:
        model = Transaction
        fields = ['share', 'type', 'portfo', 'date', 'price', 'quantity']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_share(self):
        share_symbol = self.cleaned_data['share']
        try:
            share_instance = Share.objects.get(symbol=share_symbol)
        except Share.DoesNotExist:
            raise forms.ValidationError(f'Share with symbol {share_symbol} does not exist.')
        return share_instance

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.share = self.cleaned_data['share']
        if commit:
            instance.save()
        return instance
