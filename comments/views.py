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
            post = Post.objects.get(id=pk)

            new_comment = Comentario(texto=new_text, post=post)
            new_comment.save()
            
            return redirect('detalhes_post', pk=pk)