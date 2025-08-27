from django.db import models
from heroes.models import DimHero

# Create your models here.
class FactPost(models.Model):
    author = models.ForeignKey(DimHero, on_delete=models.CASCADE, related_name="posts")
    message = models.TextField()
    image = models.ImageField(upload_to='posts/')
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.code_name}: {self.message[:30]}..."


class FactLike(models.Model):
    hero = models.ForeignKey(DimHero, on_delete=models.CASCADE)
    post = models.ForeignKey(FactPost, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('hero', 'post')

    def __str__(self):
        return f"{self.hero.code_name} liked {self.post.pk}"


class FactComment(models.Model):
    post = models.ForeignKey(FactPost, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=False)
    hero = models.ForeignKey(DimHero, on_delete=models.CASCADE, null=False)
    pinned = models.BooleanField(null=False)

    def __str__(self):
        return f"{self.hero.code_name} comented: {self.comment[:30]} on {self.post.author}'s post"

    