from django.contrib import admin
from .models import Comentario

# Register your models here.
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):   
    list_display = ('id', 'texto', 'autor', 'post', 'data')
    list_filter = ('data', 'autor')
    search_fields = ('texto', 'autor__codinome', 'post__titulo')