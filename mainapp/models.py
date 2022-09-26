from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=127)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post = models.TextField()
    raiting = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment


