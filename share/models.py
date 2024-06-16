from django.db import models
from django.contrib.auth.models import User

class Share(models.Model):
    share_id        = models.AutoField(primary_key=True, db_index=True)
    symbol          = models.CharField(max_length=100)
    title           = models.CharField(max_length=300)
    group           = models.CharField(max_length=200)
    
    def __str__(self):
        return self.symbol
    
class SharePrice(models.Model):
    share = models.ForeignKey(Share, on_delete=models.PROTECT, related_name='shares2prices')
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    adj_close = models.FloatField()
    value = models.BigIntegerField()
    volume = models.BigIntegerField()
    count = models.IntegerField()
    yesterday = models.FloatField()
    close = models.FloatField()

    @property
    def symbol(self):
        return self.share.symbol

    def __str__(self):
        return f"{self.symbol} on {self.date}"

class MinMax(models.Model):
    date = models.DateField()
    share = models.ForeignKey(Share, on_delete=models.CASCADE, related_name='share2minmax')
    min = models.IntegerField()
    max = models.IntegerField()

    def __str__(self):
        return f"{self.share} - Min:{self.min} Max:{self.max}"

class DailyPrice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_prices')
    date = models.DateField()
    gold_price = models.DecimalField(max_digits=10, decimal_places=2)
    dollar_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.date} - {self.user.username}"