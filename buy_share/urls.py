from django.urls import path

from . import views

urlpatterns = [
    path('buy_share_list', views.BuyShareView.as_view(), name='buy_share_list'),
]