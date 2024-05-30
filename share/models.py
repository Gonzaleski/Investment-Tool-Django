from django.db import models
from django.contrib.auth.models import User
from pytse_client import Ticker
import persian
from django.core.cache import cache

class Share(models.Model):
    share_id        = models.AutoField(primary_key=True, db_index=True)
    symbol          = models.CharField(max_length=100)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_price   = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_price   = models.DecimalField(max_digits=10, decimal_places=2)

    # @property
    # def test(self):
    #     try:
    #         share_price_data = cache.get('share_price_data')
    #         if share_price_data is None:
    #             # Fetch fresh data from the website
    #             share_price_data = Ticker(persian.convert_ar_characters(self.symbol)).get_ticker_real_time_info_response().last_price
    #             cache.set(str(self.symbol), share_price_data, timeout=300)  # Cache for 5 minutes
    #         return share_price_data
    #     except Share.DoesNotExist:
    #         return "N/A"
    #     except Exception as e:
    #         return f"Error: {e}"  # Print any potential errors for debugging
    
    def __str__(self):
        return self.symbol

class DailyPrice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_prices')
    date = models.DateField(auto_now_add=True)
    gold_price = models.DecimalField(max_digits=10, decimal_places=2)
    dollar_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('user', 'date')
    
    def __str__(self):
        return f"{self.date} - {self.user.username}"