from django.contrib import admin
from .models import Villain

# Register your models here.
@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder', 'cidade', 'visto_por_ultimo', 'historia']
    list_filter = ['cidade', 'visto_por_ultimo']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poder', 'cidade', 'historia', 'visto_por_ultimo')
        }),
        ('Dados de Registro', {
            'fields': ('data_criacao',)
        })
    )

    readonly_fields = ['data_criacao']