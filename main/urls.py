from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import MusicView, CategoryListView, FavoritesView, CommentView, MusicListView

router = DefaultRouter()
router.register('music', MusicView)
router.register('category', CategoryListView)
router.register('favorites', FavoritesView)
router.register('comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('music_list/', MusicListView.as_view()),
]
