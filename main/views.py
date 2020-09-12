from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CategorySerializer, AuthorSerializer
from .models import Post, Author, Category


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().select_related('author', 'category')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Post.objects.filter(category_id=pk).select_related('author', 'category')


class AuthorPostListView(PostListView):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Post.objects.filter(author_id=pk).select_related('author', 'category')
