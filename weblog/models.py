from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels

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
    project_completion = jmodels.jDateTimeField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=(['-created']))
        ]

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        for img in self.portfolio_images.all():
            storage, path = img.image.storage, img.image.path
            storage.delete(path)
        super().delete(*args, **kwargs)


class PortfolioImage(models.Model):
    # relation
    author = models.ForeignKey(Portfolio, related_name='portfolio_images', on_delete=models.CASCADE)
    # data
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/')
    description = models.TextField()
    # date
    created = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=(['-created']))
        ]

    def __str__(self):
        return self.title


class Blog(models.Model):
    # blog category
    CATEGORY_CHOICES = (
        ('زبان برنامه نویسی', 'زبان برنامه نویسی'),
        ('طراحی سایت', 'طراحی سایت'),
        ('سئو', 'سئو'),
        ('UI و UX', 'UI و UX'),
        ('سایر', 'سایر'),
    )
    # relation
    author = models.ForeignKey(User, related_name='user_blogs', on_delete=models.CASCADE, default='1')
    # data
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='سایر')
    # date
    created = jmodels.jDateField(auto_now_add=True)
    updated = jmodels.jDateField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=(['-created']))
        ]

    def __str__(self):
        return self.title
