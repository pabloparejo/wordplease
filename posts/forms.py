from django.forms import ModelForm
from posts.models import Post

__author__ = 'parejo'

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ("author", "pub_date")
        fields = ("title", "image", "summary", "content", "categories")