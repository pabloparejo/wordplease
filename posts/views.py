from django.contrib.auth.models import User
from django.shortcuts import redirect
from posts.forms import PostForm
from posts.models import Post
# Create your views here.
from django.views.generic import ListView, DetailView, FormView


class BlogListView(ListView):
    template_name = "posts/blog_list.html"
    def get_queryset(self):
        #users who have posts ids gte 1
        return User.objects.filter(post__isnull=False)


class PostDetailView(DetailView):
    paginate_by = 8
    def get_queryset(self):
        return Post.published_posts()


class PostListView(ListView):
    paginate_by = 8
    def get_queryset(self):
        username = self.kwargs.get("username")
        return Post.published_posts().filter(author__username=username)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['blog_author'] = self.kwargs.get("username")
        return context


class RecentPostsListView(ListView):
    paginate_by = 8
    template_name = "posts/recent_posts_list.html"
    def get_queryset(self):
        return Post.published_posts().order_by("-pub_date")


class NewPostFormView(FormView):
    form_class = PostForm
    template_name = "posts/new_post.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect("post", self.object.author, self.object.pk)
