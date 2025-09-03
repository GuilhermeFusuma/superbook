from django.urls import path
from . import  views

urlpatterns = [
    path('lista/', views.lista_posts, name="lista_posts"),
    path('cbvlista/', views.PostsLista.as_view(), name="lista_cbv_posts"),
    path('novo/', views.criar_post, name="criar_post")
]