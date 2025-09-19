from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Comentario
from .forms import ComentarioForm
from posts.models import Post


# Create your views here.
def salvar_comentario(request, pk):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():

            new_text = form.cleaned_data['texto']
            new_autor = form.cleaned_data['autor']
            post = Post.objects.get(id=pk)

            new_comment = Comentario(texto=new_text, autor=new_autor, post=post)
            new_comment.save()
            
            return redirect('detalhe_post', pk=pk)