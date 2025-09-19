from django.db import models
from posts.models import Post
from heroes.models import Hero

# Create your models here.
class Comentario(models.Model):
    texto = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name="comentarios")
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(auto_now_add=True)