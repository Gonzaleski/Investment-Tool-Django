import django_tables2 as tables
from django.utils.html import format_html
from .models import Transaction
from django.urls import reverse_lazy
import jdatetime

class TransactionTable(tables.Table):
    type = tables.Column(orderable=False)
    user = tables.Column(orderable=False, visible=False)
    symbol = tables.Column(orderable=False)
    portfo = tables.Column(orderable=False)
    date = tables.Column(orderable=False)
    price = tables.Column(orderable=False)
    quantity = tables.Column(orderable=False)
    total = tables.Column(orderable=False)
    dollar_price = tables.Column(orderable=False)
    gold_price = tables.Column(orderable=False)
    dollar_gain = tables.Column(orderable=False)
    gold_gain = tables.Column(orderable=False)
    
    actions = tables.Column(orderable=False, empty_values=(), verbose_name='Actions')

    def render_date(self, value):
        # Convert Gregorian date to Jalali date
        gregorian_date = value
        jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
        return jalali_date.strftime('%Y-%B-%d')

    def render_actions(self, record):
        update_url = reverse_lazy('transaction_update', args=[record.pk])
        delete_url = reverse_lazy('transaction_delete', args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm">Edit</a> '
            '<a href="{}" class="btn btn-danger btn-sm">Delete</a>',
            update_url, delete_url
        )

    class Meta:
        model = Transaction
        template_name = "django_tables2/bootstrap4.html"
        fields = ('type', 'symbol', 'portfo', 'date', 'price', 'quantity', 'total', 'dollar_price', 'gold_price', 'dollar_gain', 'gold_gain')
        per_page = 30
