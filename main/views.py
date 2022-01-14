from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.filter import MusicFilter
from main.models import Category, Music, Comment, Favorites, Likes, Rating
from main.permissions import IsAdmin, IsAuthor
from main.serializers import CategorySerializer, MusicListSerializer, CommentSerializer, FavoritesSerializer, \
    MusicSerializer, RatingSerializer


# class CategoryListView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]

    def get_permissions(self):
        if self.action == 'list':
            return []
        return [IsAdmin()]


# class MusicListView(ListAPIView):
#     queryset = Music.objects.all()
#     serializer_class = MusicListSerializer


class MusicView(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_class = MusicFilter
    search_fields = ['category__name']
    ordering_fields = ['name']

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return [AllowAny()]

    @action(['POST'], detail=True)
    def add_to_liked(self, request, pk):
        music = self.get_object()
        if request.user.is_authenticated:
            if request.user.liked.filter(music=music).exists():
                return Response('Вы уже лайкнули')
            Likes.objects.create(music=music, user=request.user)
            return Response('Вы лайкнули')
        return Response('Вы не авторизованы')

    @action(['POST'], detail=True)
    def remove_from_liked(self, request, pk):
        music = self.get_object()
        if request.user.is_authenticated:
            if not request.user.liked.filter(music=music).exists():
                return Response('Вы не лайкнули')
            request.user.liked.filter(music=music).delete()
            return Response('Вы убрали лайк')
        return Response('Вы не авторизованы')

    @action(['POST'], detail=True)
    def add_to_favorites(self, request, pk):
        music = self.get_object()
        if request.user.is_authenticated:
            if request.user.favorites.filter(music=music).exists():
                return Response('Уже в избранных')
            Favorites.objects.create(music=music, user=request.user)
            return Response('Вы добавили в избранное')
        return Response('Вы не авторизованы')

    @action(['POST'], detail=True)
    def remove_from_favorites(self, request, pk):
        music = self.get_object()
        if request.user.is_authenticated:
            if not request.user.favorites.filter(music=music).exists():
                return Response('Нет в избранных')
            request.user.favorites.filter(music=music).delete()
            return Response('Вы убрали из избранных')
        return Response('Вы не авторизованы')


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_permissions(self):
    #     if self.action in []:
    #         return []
    #     return [IsAdmin()]

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return [AllowAny()]


class FavoritesView(ListAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print('ffffff')
        if not request.user.is_authenticated:
            return Response('Вы не авторизованы')
        return Response('hhhhhh')

    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [IsAuthenticated()]
    #     if self.action == 'destroy':
    #         return [IsAuthor()]
    #     return [IsAuthor()]


class RatingView(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAuthor()]
        return [IsAuthenticated()]
