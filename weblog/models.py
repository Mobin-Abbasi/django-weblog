from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Portfolio(models.Model):
    # relation
    author = models.ForeignKey(User, related_name='user_portfolios', on_delete=models.CASCADE, default='1')
    # data
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    # date
    project_completion = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=(['-created']))
        ]

    def __str__(self):
        return self.title
