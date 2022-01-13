from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import MusicView, CommentView, CategoryView, FavoritesView

router = DefaultRouter()
router.register('music', MusicView)
router.register('category', CategoryView)
router.register('favorites', FavoritesView)
router.register('comment', CommentView)
# router.register('like', LikeView)

urlpatterns = [
    path('', include(router.urls)),
]
