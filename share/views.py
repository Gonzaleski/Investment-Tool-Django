from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Share, DailyPrice
from .tables import ShareTable, DailyPricesTable
from .forms import ShareFilterForm, DailyPriceForm
from django.db.models import Q

class ShareView(LoginRequiredMixin, SingleTableView):
    model = Share
    table_class = ShareTable
    context_object_name = 'shares'
    template_name = 'share/share.html'
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search and filter logic
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(symbol__icontains=search_query)
            )

        form = ShareFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['symbol']:
                queryset = queryset.filter(symbol__icontains=form.cleaned_data['symbol'])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ShareFilterForm(self.request.GET)
        context['search_query'] = self.request.GET.get('search', '')
        
        return context

class DailyPriceView(LoginRequiredMixin, SingleTableView):
    model = DailyPrice
    table_class = DailyPricesTable
    context_object_name = 'daily_prices'
    template_name = 'share/daily_price_list.html'
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset

class DailyPriceCreateView(LoginRequiredMixin, CreateView):
    model = DailyPrice
    form_class = DailyPriceForm
    template_name = 'share/daily_price_form.html'
    success_url = reverse_lazy('daily_price_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DailyPriceUpdateView(LoginRequiredMixin, UpdateView):
    model = DailyPrice
    form_class = DailyPriceForm
    template_name = 'share/daily_price_form.html'
    success_url = reverse_lazy('daily_price_list')
    login_url = 'login'

    def get_queryset(self):
        return DailyPrice.objects.filter(user=self.request.user)

class DailyPriceDeleteView(LoginRequiredMixin, DeleteView):
    model = DailyPrice
    template_name = 'share/daily_price_confirm_delete.html'
    success_url = reverse_lazy('daily_price_list')
    login_url = 'login'

    def get_queryset(self):
        return DailyPrice.objects.filter(user=self.request.user)