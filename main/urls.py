from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import MusicView, CommentView, CategoryView, FavoritesView, RatingView

router = DefaultRouter()
router.register('music', MusicView)
router.register('category', CategoryView)
router.register('comment', CommentView)
router.register('rating', RatingView)

urlpatterns = [
    path('', include(router.urls)),
    path('favorites_list/', FavoritesView.as_view()),
]
