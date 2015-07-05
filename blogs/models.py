from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):

    user = models.ForeignKey(User)

    categories = models.ManyToManyField(Category)
    content = models.TextField()
    pub_date = models.DateField(auto_now=True)
    summary = models.TextField()
    thumbnail = models.URLField(default="static/img/post-default.jpg")
    title = models.CharField(max_length=255)

class Category(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now=True)