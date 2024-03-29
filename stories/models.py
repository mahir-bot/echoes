from email.policy import default
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Stories(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnil = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50]+'........'
