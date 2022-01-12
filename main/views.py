from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from main.models import Category, Music, Comment, Favorites
from main.permissions import IsAdmin
from main.serializers import CategorySerializer, MusicListSerializer, CommentSerializer, FavoritesSerializer, \
    MusicSerializer


class CategoryListView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MusicListView(ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicListSerializer


class MusicView(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAdmin]


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FavoritesView(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

