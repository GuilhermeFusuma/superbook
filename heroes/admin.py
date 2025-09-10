from django.contrib import admin
from .models import Hero

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder', 'cidade', 'data_criacao']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']
