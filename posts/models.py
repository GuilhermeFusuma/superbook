from django.db import models
from heroes.models import Hero

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="posts")
    mensagem = models.TextField()
    imagem = models.ImageField(upload_to='posts/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.codinome}: {self.mensagem[:30]}..."



    