from .models import Stock
from django.views.generic import ListView
from django_q.tasks import schedule
from django_q.models import Schedule
from django.shortcuts import render

schedule('stock.tasks.update_stock_info', schedule_type=Schedule.MINUTES, minutes=5, repeats=-1)

class StockListView(ListView):
    model = Stock
    template_name = 'home.html'