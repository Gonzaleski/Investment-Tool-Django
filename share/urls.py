from django.urls import path

from . import views

urlpatterns = [
    path('shares', views.ShareView.as_view(), name='shares'),
    path('shares/add/', views.ShareCreateView.as_view(), name='share_add'),
    path('prices/', views.DailyPriceListView.as_view(), name='daily_price_list'),
    path('prices/edit/', views.DailyPriceUpdateView.as_view(), name='daily_price_update'),
]