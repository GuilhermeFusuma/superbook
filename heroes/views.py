from django.shortcuts import render
from .models import DimHero

def lista_herois(request):
    herois = DimHero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"herois": herois})
