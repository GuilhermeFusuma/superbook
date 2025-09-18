from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Hero
from .forms import ContactForm, HeroForm

#FBV - function-based view - view baseada em função
def lista_herois(request):
    herois = Hero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"herois": herois})

#CBV - CLASS-BASED VIEW - VIEW BASEADA EM CLASSE COM GENERIC LIST VIEW
class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"

def contato_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            print(form.cleaned_data)
            return render(request, "heroes/contato_sucesso.html")
    else:
        form = ContactForm()

    return render(request, "heroes/contato.html", {"form": form})

class HeroCreateView(CreateView):
    model = Hero
    form_class = HeroForm
    template_name = 'heroes/form_heroi.html'
    success_url = reverse_lazy('lista_herois')