from django.shortcuts import render
from django.views.generic import ListView
from produtos.models import Produto

class ProdutoListView(ListView):
  model = Produto