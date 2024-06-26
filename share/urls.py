from django.urls import path
from .views import ShareView, DailyPriceView, SharePriceView, DailyPriceCreateView, DailyPriceUpdateView, DailyPriceDeleteView

urlpatterns = [
    path('shares', ShareView.as_view(), name='shares'),
    path('shares/daily-prices/', DailyPriceView.as_view(), name='daily_price_list'),
    path('shares/daily-prices/add/', DailyPriceCreateView.as_view(), name='daily_price_add'),
    path('shares/daily-prices/update/<int:pk>/', DailyPriceUpdateView.as_view(), name='daily_price_update'),
    path('shares/daily-prices/delete/<int:pk>/', DailyPriceDeleteView.as_view(), name='daily_price_delete'),
    path('shares/prices', SharePriceView.as_view(), name='share_price_list'),
]
