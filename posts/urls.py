from django.urls import path
from .views import lista_posts, PostsLista

urlpatterns = [
    path('lista/', lista_posts, name="lista_posts"),
    path('cbvlista/', PostsLista.as_view(), name="lista_cbv_posts"),
]