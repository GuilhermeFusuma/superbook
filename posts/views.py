from django.shortcuts import render
from .models import FactPost

# Create your views here.
def lista_posts(request):
    posts = FactPost.objects.all()
    return render(request, "posts/lista_posts.html", {"posts": posts})

