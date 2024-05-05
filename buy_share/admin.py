from django.contrib import admin

from . import models

class SellShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'share', 'user', 'portfo', 'date', 'price', 'dollar_price', 'gold_price', 'quantity', 'total', 'dollar_gain', 'gold_gain')
    
admin.site.register(models.BuyShare, SellShareAdmin)