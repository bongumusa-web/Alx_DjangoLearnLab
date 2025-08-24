from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, UserViewSet, FeedView

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),

    # Explicit like and unlike endpoints for posts
    path("posts/<int:pk>/like/", PostViewSet.as_view({"post": "like"}), name="post-like"),
    path("posts/<int:pk>/unlike/", PostViewSet.as_view({"post": "unlike"}), name="post-unlike"),
]
