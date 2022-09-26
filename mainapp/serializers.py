from rest_framework import serializers

from mainapp.models import(
    User, Post, Comment
)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'post', 'raiting', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'comment', )
        read_only_fields = ('created_at', )