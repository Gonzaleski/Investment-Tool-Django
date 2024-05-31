from django.contrib import admin

from . import models

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'symbol', 'portfo', 'date', 'price', 'quantity', 'total', 'dollar_price', 'gold_price', 'dollar_gain', 'gold_gain')

admin.site.register(models.Transaction, TransactionAdmin)