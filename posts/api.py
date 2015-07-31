#encoding:UTF:8
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import BlogSerializer, PostSerializer, PostListSerializer, PostDetailSerializer
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
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
        author = get_object_or_404(User, username=self.kwargs.get("username"))
        if user.is_anonymous():
            return Post.published_posts().filter(author=author)
        else:
            if user.is_staff:
                return Post.objects.filter(author=author)
            else:
                return Post.objects.filter(Q(author=author) & (Q(author=user) | Q(pub_date__lte=timezone.now())))

    def get_serializer_class(self):
        if self.action:
            if self.action.upper() == "LIST":
                return PostListSerializer
            elif self.action.upper() == "RETRIEVE":
                return PostDetailSerializer

        return PostSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class NewPostApi(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)
