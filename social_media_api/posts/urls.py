from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, UserViewSet

from .views import FeedView


router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"users", UserViewSet) 

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
]
