from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hero(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hero', null=True, blank=True) 

    codinome = models.CharField(max_length=50, unique=True, blank=True, null=True)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    historia = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    email_contato = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.ImageField(upload_to='fotos_herois/', default='fotos_herois/default_profile.png', blank=True, null=True)

    def __str__(self):
        return self.codinome

    
# class Follow(models.Model):
#     follower = models.ForeignKey(DimHero, on_delete=models.CASCADE, null=False)
#     following = models.ForeignKey(DimHero, on_delete=models.CASCADE, null=False)

#     class Meta:
#         unique_together = ('follower', 'following')

#     def __str__(self):
#         return f'{self.follower} follows {self.following}'

# class Block(models.Model):
#     blocker = models.ForeignKey(DimHero, on_delete=models.CASCADE, null=False)
#     blocked = models.ForeignKey(DimHero, on_delete=models.CASCADE, null=False)

#     class Meta:
#         unique_together = ('blocker', 'blocked')

#     def __str__(self):
#         return f'{self.blocker} blocked {self.blocked}'