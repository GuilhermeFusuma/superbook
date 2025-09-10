from django.contrib import admin
from .models import Post, Like, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = [
        "autor",
        "mensagem",
        "imagem",
        "data_criacao"
    ]

class LikeAdmin(admin.ModelAdmin):
    fields = [
        "hero",
        "post",
        "data_criacao"
    ]

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)