from django.db import models

from users_xone.models import User


class Link(models.Model):
    TYPES = (
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(unique=True)
    image = models.URLField(null=True, blank=True)
    link_type = models.CharField(max_length=255, choices=TYPES, default='website')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    links = models.ManyToManyField(Link, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
