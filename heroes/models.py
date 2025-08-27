from django.db import models

# Create your models here.
class DimHero(models.Model):
    code_name = models.CharField(max_length=50, unique=True)
    real_name = models.CharField(max_length=100, blank=True, null=True)
    power = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    history = models.TextField(blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code_name

    
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