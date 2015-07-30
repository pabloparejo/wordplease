#encoding:UTF:8
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import BlogSerializer, PostSerializer, PostListSerializer
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet


class BlogsAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Post.get_authors()



class PostsViewSet(ModelViewSet):
    """
    Endpoint para poder leer los artículos de un blog:
        si el usuario no está autenticado, mostrará sólo los artículos públicos.
        Si el usuario está autenticado y es el propietario del blog o un administrador, podrá ver todos los artículos (públicos o no).
        En este endpoint se deberá mostrar únicamente el título del post, la imagen, el resumen y la fecha de publicación.
        Este endpoint debe permitir buscar posts por título o contenido y ordenarlos por título o fecha de publicación.
        Por defecto los posts deberán venir ordenados por fecha de publicación descendente.
    """
    model = Post
    permission_classes = (PostPermissions,)

    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ("title", "pub_date")
    search_fields = ("title", "content", "summary")

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous():
            return Post.published_posts()
        else:
            if user.is_staff:
                return Post.objects.all()
            else:
                return Post.objects.filter(Q(author=user) | Q(pub_date__lte=timezone.now()))

    def get_serializer_class(self):
        if self.action:
            if self.action.upper() == "LIST":
                return PostListSerializer

        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
