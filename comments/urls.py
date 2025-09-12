from django.urls import path
from . import views

urlpatterns = [
    path('salvar_comentario/<int:pk>/', views.salvar_comentario, name="salvar_comentario"),
]