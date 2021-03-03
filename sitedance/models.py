from django.db import models
from django.utils import timezone


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)


class MyClass(models.Model):
    userId = models.CharField(max_length=20)
    personType = (
        ()
    )
