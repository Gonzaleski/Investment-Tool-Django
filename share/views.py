from django_tables2 import SingleTableView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Share
from .tables import ShareTable

class ShareView(LoginRequiredMixin, SingleTableView):
    model = Share
    table_class = ShareTable
    context_object_name = 'share'
    template_name = 'share/share.html'
    login_url = 'login'