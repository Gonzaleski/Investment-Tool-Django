# views.py
from django_tables2 import SingleTableView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.db.models import Q
from .models import Transaction
from .tables import TransactionTable
from .forms import TransactionFilterForm, TransactionForm

from django.http import JsonResponse
from share.models import Share

class TransactionView(LoginRequiredMixin, SingleTableView):
    model = Transaction
    table_class = TransactionTable
    context_object_name = 'transactions'
    template_name = 'transactions/transactions.html'
    login_url = 'login'
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        
        # Search and filter logic
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(share__symbol__icontains=search_query)
            )
        
        form = TransactionFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['type']:
                queryset = queryset.filter(type=form.cleaned_data['type'])
            if form.cleaned_data['portfo']:
                queryset = queryset.filter(portfo__icontains=form.cleaned_data['portfo'])
            if form.cleaned_data['date_from']:
                queryset = queryset.filter(date__gte=form.cleaned_data['date_from'])
            if form.cleaned_data['date_to']:
                queryset = queryset.filter(date__lte=form.cleaned_data['date_to'])
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TransactionFilterForm(self.request.GET)
        context['search_query'] = self.request.GET.get('search', '')
        return context
    
class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions')
    login_url = 'login'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
class ShareAutocomplete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if 'term' in request.GET:
            qs = Share.objects.filter(symbol__icontains=request.GET.get('term'))
            symbols = list()
            for share in qs:
                symbols.append(share.symbol)
            return JsonResponse(symbols, safe=False)
        return JsonResponse([], safe=False)
