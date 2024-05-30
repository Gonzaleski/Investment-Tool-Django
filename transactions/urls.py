from django.urls import path
from .views import TransactionView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView

from . import views

urlpatterns = [
    path('transactions', views.TransactionView.as_view(), name='transactions'),
    path('transactions/add/', TransactionCreateView.as_view(), name='transaction_add'),
    path('transactions/update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),
]