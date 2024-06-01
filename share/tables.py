import django_tables2 as tables
from .models import Share, DailyPrice
from django.urls import reverse_lazy
from django.utils.html import format_html

class ShareTable(tables.Table):
    symbol = tables.Column(orderable=False)
    price = tables.Column(orderable=False)
    minimum_price = tables.Column(orderable=False)
    maximum_price = tables.Column(orderable=False)

    class Meta:
        model = Share
        template_name = "django_tables2/bootstrap4.html"
        fields = ('symbol', 'price', 'minimum_price', 'maximum_price')
        attrs = {'class': 'table'}
        per_page = 30

class DailyPricesTable(tables.Table):
    user = tables.Column(orderable=False, visible=False)
    date = tables.Column(orderable=False)
    dollar_price = tables.Column(orderable=False)
    gold_price = tables.Column(orderable=False)
    
    actions = tables.Column(orderable=False, empty_values=(), verbose_name='Actions')

    def render_actions(self, record):
        update_url = reverse_lazy('daily_price_update', args=[record.pk])
        delete_url = reverse_lazy('daily_price_delete', args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm">Edit</a> '
            '<a href="{}" class="btn btn-danger btn-sm">Delete</a>',
            update_url, delete_url
        )

    class Meta:
        model = DailyPrice
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date', 'dollar_price', 'gold_price')
        per_page = 30
