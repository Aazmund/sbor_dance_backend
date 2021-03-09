from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок новости")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    body = RichTextUploadingField(max_length=10000, verbose_name="Содержимое")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name="Статус")
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ('-publish',)


class MyClass(models.Model):
    userId = models.CharField(max_length=20)
    personType = (
        ()
    )
