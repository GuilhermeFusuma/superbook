from django.db import models
from heroes.models import Hero

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="posts")
    mensagem = models.TextField()
    imagem = models.ImageField(upload_to='posts/')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.codinome}: {self.mensagem[:30]}..."


class Like(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('hero', 'post')

    def __str__(self):
        return f"{self.hero.codinome} liked {self.post.pk}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=False)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, null=False)
    pinned = models.BooleanField(null=False)

    def __str__(self):
        return f"{self.hero.codinome} comented: {self.comment[:30]} on {self.post.autor}'s post"

    