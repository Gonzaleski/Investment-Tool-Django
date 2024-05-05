from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BuyShare
from .tables import BuyShareTable

class BuyShareView(LoginRequiredMixin, SingleTableView):
    model = BuyShare
    table_class = BuyShareTable
    context_object_name = 'buyshare'
    template_name = 'buy_share/buy_share.html'
    login_url = 'login'