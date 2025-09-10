from django.contrib import admin
from .models import Post, Like, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['autor', 'mensagem', 'imagem', 'data_criacao'] # campos exibidos
    # list_filter = ['autor'] # campos para serem filtrados
    search_fields = ['autor', 'mensagem'] 

    # fieldsets = (
    #     ('')
    # )

# admin.site.register(Post)
# admin.site.register(Like)
# admin.site.register(Comment)