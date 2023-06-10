from django.contrib import admin

from .models import Image, Like, Comment

# Register your models here.

admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Comment)
