from django.contrib import admin

# Register your models here.
from sitedance.models import Post, SportPost

admin.site.register(Post)
admin.site.register(SportPost)
