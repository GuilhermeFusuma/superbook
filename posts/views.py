from django.views.generic import ListView
from django.shortcuts import render
from .models import FactPost

# Feito por Guilherme Fusuma

# Create your views here.
def lista_posts(request):
    posts = FactPost.objects.all()
    return render(request, "posts/lista_posts.html", {"posts": posts})

class PostsLista(ListView):
    model = FactPost
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
