import django_tables2 as tables
from .models import Share, SharePrice, DailyPrice
from django.urls import reverse_lazy
from django.utils.html import format_html
import jdatetime

class ShareTable(tables.Table):
    symbol = tables.Column(orderable=False)

    class Meta:
        model = Share
        template_name = "django_tables2/bootstrap4.html"
        fields = ('symbol',)
        attrs = {'class': 'table'}
        per_page = 30

class SharePricesTable(tables.Table):
    symbol = tables.Column(accessor='share.symbol', verbose_name='Symbol')
    date = tables.DateColumn(format='Y-m-d', verbose_name='Date')
    datetime = tables.DateTimeColumn(verbose_name='Date Time')
    open = tables.Column(verbose_name='Open')
    high = tables.Column(verbose_name='High')
    low = tables.Column(verbose_name='Low')
    adj_close = tables.Column(verbose_name='Adj Close')
    value = tables.Column(verbose_name='Value')
    volume = tables.Column(verbose_name='Volume')
    count = tables.Column(verbose_name='Count')
    yesterday = tables.Column(verbose_name='Yesterday')
    close = tables.Column(verbose_name='Close')

    class Meta:
        model = SharePrice
        template_name = "django_tables2/bootstrap4.html"
        fields = ('symbol', 'date', 'datetime', 'open', 'high', 'low', 'adj_close', 'value', 'volume', 'count', 'yesterday', 'close')
        attrs = {'class': 'table'}
        per_page = 30

class DailyPricesTable(tables.Table):
    user = tables.Column(orderable=False, visible=False)
    date = tables.Column(orderable=False)
    dollar_price = tables.Column(orderable=False)
    gold_price = tables.Column(orderable=False)
    
    actions = tables.Column(orderable=False, empty_values=(), verbose_name='Actions')

    def render_date(self, value):
        # Convert Gregorian date to Jalali date
        gregorian_date = value
        jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
        return jalali_date.strftime('%Y-%B-%d')

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
