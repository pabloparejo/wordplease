from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now=True)

class Post(models.Model):

    author = models.ForeignKey(User)

    categories = models.ManyToManyField(Category, blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_created=True, default=timezone.now)
    summary = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.user.username + " - " + self.title