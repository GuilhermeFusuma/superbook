from django.urls import path
from . import  views

urlpatterns = [
    path('lista/', views.PostListView.as_view(), name="lista_posts"),
    path('novo/', views.PostCreateView.as_view(), name="novo_post"),
    path('editar/<int:pk>/', views.PostUpdateView.as_view(), name='editar_post'),
    path('excluir/<int:pk>/', views.PostDeleteView.as_view(), name='excluir_post'),
]