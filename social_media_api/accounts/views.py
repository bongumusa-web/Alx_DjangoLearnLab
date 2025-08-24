from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .serializers import RegisterSerializer, UserSerializer
from notifications.models import Notification

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({
            "token": token.key,
            "user_id": token.user_id,
            "username": token.user.username,
        })


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        request.user.following.add(user_to_follow)

        # Create notification (avoid self-notify)
        if user_to_follow != request.user:
            Notification.objects.create(
                recipient=user_to_follow,
                actor=request.user,
                verb="started following you",
                content_type=ContentType.objects.get_for_model(user_to_follow),
                object_id=user_to_follow.id
            )

        return Response({"status": f"You followed {user_to_follow.username}"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"status": f"You unfollowed {user_to_unfollow.username}"})
