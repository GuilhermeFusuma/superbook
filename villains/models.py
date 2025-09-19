from django.db import models

# Create your models here.
class Villain(models.Model):
    codinome = models.CharField(max_length=50, unique=True)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    visto_por_ultimo = models.TextField(max_length=200, null=True, blank=True)
    historia = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='villains/', blank=True, null=True)

    def __str__(self):
        return self.codinome
