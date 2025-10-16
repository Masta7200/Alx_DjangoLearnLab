from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedView, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

# Nested router for comments
posts_router = DefaultRouter()
posts_router.register(r'posts/(?P<post_pk>[^/.]+)/comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
     path('feed/', FeedView.as_view(), name='user-feed'),
]
