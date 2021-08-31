from django.db import models

# Create your models here.
class BtcRate(models.Model):
    name = models.CharField(max_length=256)
    currency = models.CharField(max_length=256)
    exchange_rate = models.CharField(max_length=256)
    last_refresh = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exchange_rate