from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "author_username", "content", "created_at", "updated_at"]
        read_only_fields = ["author"]


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)  # NEW

    class Meta:
        model = Post
        fields = [
            "id", "author", "author_username", "title", "content",
            "created_at", "updated_at", "comments", "likes_count"
        ]
        read_only_fields = ["author"]
