from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.VillainListView.as_view(), name='lista_viloes'),
]

