from django.contrib.auth.models import User
from posts.models import Post
# Create your views here.
from django.views.generic import ListView, DetailView




class BlogListView(ListView):
    template_name = "posts/blog_list.html"
    def get_queryset(self):

        return User.objects.filter(pk__in=Post.published_posts().values('author__pk'))


class PostDetailView(DetailView):
    def get_queryset(self):
        return Post.published_posts()


class PostListView(ListView):
    def get_queryset(self):
        username = self.kwargs.get("username")
        return Post.published_posts().filter(author__username=username)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['blog_author'] = self.kwargs.get("username")
        return context


class RecentPostsListView(ListView):
    template_name = "posts/recent_posts_list.html"
    def get_queryset(self):
        return Post.published_posts().order_by("pub_date")
