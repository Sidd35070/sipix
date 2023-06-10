from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    description = models.TextField(null=True, blank=True)
    photographer = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    createdAt = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    imageUrl = models.TextField(null=False, blank=False)
    likesCount = models.IntegerField(null=True, blank=True, default=0)
    commentCount = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.description
    

class Like(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null = True)
    likedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null = True)
    commentedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    commentedAt = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=False, blank=False)


    def __str__(self):
        return self.comment

