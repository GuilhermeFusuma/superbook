from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from comments.models import Comentario
from comments.forms import ComentarioForm
from .models import Post
from .forms import PostForm


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/lista_posts.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')

def post_detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()
    form = ComentarioForm()

    return render(request, 'posts/detalhes_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })