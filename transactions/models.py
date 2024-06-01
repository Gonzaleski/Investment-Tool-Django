from django.db import models
from django.contrib.auth.models import User
from share.models import Share, DailyPrice

class Transaction(models.Model):
    BUY = 'BUY'
    SELL = 'SELL'
    TRANSACTION_TYPES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]

    id = models.AutoField(db_index=True, primary_key=True)
    share = models.ForeignKey(Share, on_delete=models.PROTECT, related_name='ids2transactions')
    type = models.CharField(max_length=4, choices=TRANSACTION_TYPES, default=BUY)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    portfo = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField()
    daily_price = models.ForeignKey(DailyPrice, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def total(self):
        return self.price * self.quantity if self.price and self.quantity else None

    @property
    def symbol(self):
        return self.share.symbol

    @property
    def dollar_price(self):
        return self.daily_price.dollar_price if self.daily_price else None

    @property
    def gold_price(self):
        return self.daily_price.gold_price if self.daily_price else None

    @property
    def dollar_gain(self):
        if self.dollar_price and self.quantity:
            today_price = DailyPrice.objects.latest('date').dollar_price
            return round((today_price / self.dollar_price) * (self.share.maximum_price / self.price), 2)
        return None

    @property
    def gold_gain(self):
        if self.gold_price and self.quantity:
            today_price = DailyPrice.objects.latest('date').gold_price
            return round((today_price / self.gold_price) * (self.share.maximum_price / self.price), 2)
        return None

    def save(self, *args, **kwargs):
        if not self.daily_price:
            try:
                self.daily_price = DailyPrice.objects.filter(
                    user=self.user, 
                    date__lte=self.date
                ).latest('date')
            except DailyPrice.DoesNotExist:
                raise ValueError("No DailyPrice entry available for the selected date.")
        super().save(*args, **kwargs)
