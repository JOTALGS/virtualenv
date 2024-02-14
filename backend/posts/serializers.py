from .models import Posts, PostAttachment, Comment, Trend
from rest_framework import serializers
from accounts.serializers import UserSerializer


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'get_image',)


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Posts
        fields = ('id', 'body', 'likes_count', 'comments_count', 'owner', 'created_since', 'attachments')


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'created_since',)


class PostDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Posts
        fields = ('id', 'body', 'likes_count', 'comments_count', 'owner', 'created_since', 'comments', 'attachments',)


class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ('id', 'hashtag', 'occurences',)
