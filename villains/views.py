from django.shortcuts import render
from django.views.generic import ListView
from .models import Villain

class VillainListView(ListView):
    model = Villain
    template_name = 'villains/lista_viloes.html'
    context_object_name = 'viloes'

