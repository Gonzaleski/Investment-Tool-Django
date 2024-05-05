import django_tables2 as tables
from .models import BuyShare

class BuyShareTable(tables.Table):
    id              = tables.Column(orderable=False)
    share           = tables.Column(orderable=False, accessor='share.share_id')
    user            = tables.Column(orderable=False, visible=False)
    symbol          = tables.Column(orderable=False)
    portfo          = tables.Column(orderable=False)
    date            = tables.Column(orderable=False)
    price           = tables.Column(orderable=False)
    dollar_price    = tables.Column(orderable=False)
    gold_price      = tables.Column(orderable=False)
    quantity        = tables.Column(orderable=False)
    total           = tables.Column(orderable=False)
    dollar_gain     = tables.Column(orderable=False)
    gold_gain       = tables.Column(orderable=False)

    
    class Meta:
        model = BuyShare
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', 'share', 'user', 'symbol', 'portfo', 'date', 'price', 'dollar_price', 'gold_price', 'quantity', 'total', 'dollar_gain', 'gold_gain')