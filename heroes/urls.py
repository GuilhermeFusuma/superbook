from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_herois, name='lista_herois'),
    path('cbv-lista/', views.HeroListView.as_view(), name='cbv_lista_herois'),
    path('contato/', views.contato_view, name="contato"),
    path('novo-heroi/', views.criar_heroi, name="criar_heroi")
]