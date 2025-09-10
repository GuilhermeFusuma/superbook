from django.contrib import admin
from .models import Hero

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder', 'cidade', 'data_criacao'] # campos exibidos
    list_filter = ['cidade'] # campos para serem filtrados
    search_fields = ['codinome', 'nome_real', 'cidade'] # campos que podem ser pesquisados

    fieldsets = ( # divide os campos em várias seções
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poder', 'cidade', 'historia')
        }),
        ('Dados de Registro', {
            'fields': ('data_criacao',)
        }),
    )
    readonly_fields = ['data_criacao']
