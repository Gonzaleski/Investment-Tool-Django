import django_tables2 as tables
from .models import Share

class ShareTable(tables.Table):
    symbol          = tables.Column(orderable=False)
    price           = tables.Column(orderable=False)
    minimum_price   = tables.Column(orderable=False)
    maximum_price   = tables.Column(orderable=False)
    test            = tables.Column(orderable=False)
    
    class Meta:
        model = Share
        template_name = "django_tables2/bootstrap.html"
        fields = ('symbol', 'price', 'minimum_price', 'maximum_price', 'test')