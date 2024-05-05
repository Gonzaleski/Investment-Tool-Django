from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import SellShare
from .tables import SellShareTable

class SellShareView(LoginRequiredMixin, SingleTableView):
    model = SellShare
    table_class = SellShareTable
    context_object_name = 'sellshare'
    template_name = 'sell_share/sell_share.html'
    login_url = 'login'