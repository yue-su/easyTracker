from django.shortcuts import render
from .models import Stock
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class StockListView(ListView):
    model = Stock
    template_name = 'home.html'