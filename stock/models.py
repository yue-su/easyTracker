from django.db import models
from django.urls import reverse

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.ticker
    
    def get_absolute_url(self):
        return reverse('stock_detail', args=[str(self.id)])