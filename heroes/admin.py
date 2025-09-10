from django.contrib import admin
from .models import Hero

# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'criado_em']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']


admin.site.register(Hero)