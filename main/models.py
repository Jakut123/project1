from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.SlugField(primary_key=True)
    description = models.TextField(max_length=100)
    author = models.CharField(max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='music')
    image = models.ImageField()
    music = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='music'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    music = models.ForeignKey(Music,
                              on_delete=models.CASCADE,
                              related_name='comments')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Favorites(models.Model):
    music = models.ForeignKey(Music,
                              on_delete=models.CASCADE,
                              related_name='favorites')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='liked')

    class Meta:
        unique_together = ['music', 'user']
