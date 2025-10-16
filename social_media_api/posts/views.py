from typing import List
from rest_framework import generics, permissions, viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs['post_pk'])

class FeedView(generics.ListAPIView):  # Correcting the inheritance here
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> List[Post]:
        # Fetch posts from users that the current user is following
        return Post.objects.filter(author__in=self.request.user.following.all()).order_by('-created_at')
