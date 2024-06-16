# forms.py
from django import forms
from .models import Share, DailyPrice
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django.core.exceptions import ValidationError

class DailyPriceForm(forms.ModelForm):
    class Meta:
        model = DailyPrice
        fields = ['date', 'gold_price', 'dollar_price']
    
    def __init__(self, *args, **kwargs):
        super(DailyPriceForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('date'), widget=AdminJalaliDateWidget) # date format is  "yyyy-mm-dd"
        for field_name, field in self.fields.items():
            if field_name == "date":
                field.widget.attrs.update({'class': 'form-control', 'data-jdp' : ""})
            else:
                field.widget.attrs.update({'class': 'form-control'})

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


class ShareFilterForm(forms.Form):
    symbol = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class SharePriceFilterForm(forms.Form):
    symbol = forms.CharField(max_length=100, required=False)
    # Add more fields for filtering options as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})