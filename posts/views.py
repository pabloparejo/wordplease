from django.utils import timezone
from posts.models import Post
# Create your views here.
from django.views.generic import ListView


class PostListView(ListView):
    def get_queryset(self):
        pub_posts = Post.objects.filter(pub_date__lte=timezone.now())
        return pub_posts.filter(author__username = self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['blog_author'] = self.kwargs.get("username")
        return context