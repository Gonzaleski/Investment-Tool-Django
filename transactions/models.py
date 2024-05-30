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
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()
    dollar_price = models.IntegerField(null=True, blank=True)
    gold_price = models.IntegerField(null=True, blank=True)

    @property
    def total(self):
        if self.price is not None and self.quantity is not None:
            return self.price * self.quantity

    @property
    def symbol(self):
        try:
            return self.share.symbol
        except Share.DoesNotExist:
            return "N/A"
        except Exception as e:
            return f"Error: {e}"

    @property
    def dollar_gain(self):
        today_price = DailyPrice.objects.latest('date').dollar_price
        if self.dollar_price is not None and self.quantity is not None:
            if self.type == self.BUY:
                gain = (today_price / self.dollar_price) * (self.share.maximum_price / self.price)
            elif self.type == self.SELL:
                gain = (today_price / self.dollar_price) * (self.share.minimum_price / self.price)
            return round(gain, 2)
        return None

    @property
    def gold_gain(self):
        today_price = DailyPrice.objects.latest('date').gold_price
        if self.gold_price is not None and self.quantity is not None:
            if self.type == self.BUY:
                gain = (today_price / self.gold_price) * (self.share.maximum_price / self.price)
            elif self.type == self.SELL:
                gain = (today_price / self.gold_price) * (self.share.minimum_price / self.price)
            return round(gain, 2)
        return None

    def save(self, *args, **kwargs):
        if not self.dollar_price or not self.gold_price:
            try:
                latest_price = DailyPrice.objects.latest('date')
                if not self.dollar_price:
                    self.dollar_price = latest_price.dollar_price
                if not self.gold_price:
                    self.gold_price = latest_price.gold_price
            except DailyPrice.DoesNotExist:
                pass
        super().save(*args, **kwargs)
