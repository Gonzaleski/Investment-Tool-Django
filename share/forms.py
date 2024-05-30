# forms.py
from django import forms
from .models import Share, DailyPrice

class DailyPriceForm(forms.ModelForm):
    class Meta:
        model = DailyPrice
        fields = ['gold_price', 'dollar_price']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class ShareFilterForm(forms.Form):
    symbol = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['symbol', 'price', 'minimum_price', 'maximum_price']