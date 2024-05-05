from django.db import models
from django.contrib.auth.models import User
from share.models import Share

class SellShare(models.Model):
    id              = models.AutoField(db_index=True, primary_key=True)
    share           = models.ForeignKey(Share, on_delete=models.PROTECT, related_name='ids2sells')
    user            = models.ForeignKey(User, on_delete=models.PROTECT)
    portfo          = models.CharField(max_length=100)
    date            = models.DateField()
    price           = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dollar_price    = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=00.00)
    gold_price      = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=00.00)
    quantity        = models.IntegerField()
    dollar_gain     = models.DecimalField(max_digits=10, decimal_places=2)
    gold_gain       = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total(self):
        if (self.price != None)  & (self.quantity != None):
            return self.price * self.quantity

    @property
    def symbol(self):
        try:
            return Share.objects.get(share_id=self.share.share_id).symbol
        except Share.DoesNotExist:
            return "N/A"
        except Exception as e:
            return f"Error: {e}"  # Print any potential errors for debugging