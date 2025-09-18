from django.contrib import admin
from .models import Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('codinome', 'cidade', 'data_criacao')
    search_fields = ('codinome', 'nome_real', 'cidade')
    readonly_fields = ('data_criacao',)

    fieldsets = (
        ('Identidade Secreta', {
        'fields': ('codinome', 'nome_real'),
        }),
        ('Informações Gerais', {
        'fields': ('poder', 'cidade', 'email_contato', 'historia', 'imagem'),
        }),
        ('Dados de Registro', {
        'fields': ('data_criacao',),
        'classes': ('collapse',),
        }),
    )