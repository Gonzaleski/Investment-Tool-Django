from django.urls import path

from . import views

urlpatterns = [
    path('sell_share_list', views.SellShareView.as_view(), name='sell_share_list'),
]