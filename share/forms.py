from django import forms

from .models import Share

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('symbol', 'price', 'maximum_price', 'minimum_price')