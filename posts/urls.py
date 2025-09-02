from django.urls import path
from .views import *

urlpatterns = [
    path('lista/', lista_posts , name='lista_posts'),
]