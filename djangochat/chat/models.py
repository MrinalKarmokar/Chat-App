from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
