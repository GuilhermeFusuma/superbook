from django.shortcuts import render
from .models import DimHero
from django.views.generic import ListView

def lista_herois(request):
    heroes = DimHero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"heroes": heroes})

#CBV - CLASS-BASED-VIEW view baseada em classe com generic ListV    iew
class HeroListView(ListView):
    model = DimHero
    template_name = "heroes/lista_herois.html"
    context_object_name = "heroes"