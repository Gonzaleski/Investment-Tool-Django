# forms.py
from django import forms
from .models import Share, DailyPrice
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

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