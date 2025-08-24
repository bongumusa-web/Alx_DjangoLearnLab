from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from accounts.serializers import UserSerializer  

User = get_user_model()


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only allow authors to edit/delete their own content.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Like a post
    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes.add(request.user)
        return Response({"status": "post liked"})

    # Unlike a post
    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.likes.remove(request.user)
        return Response({"status": "post unliked"})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Follow/Unfollow users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        user = self.get_object()
        request.user.followers.add(user)
        return Response({"status": f"You followed {user.username}"})

    @action(detail=True, methods=["post"])
    def unfollow(self, request, pk=None):
        user = self.get_object()
        request.user.followers.remove(user)
        return Response({"status": f"You unfollowed {user.username}"})
