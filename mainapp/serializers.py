from rest_framework import serializers

from mainapp.models import(
    User, Post, Comment
)

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    postname = serializers.ReadOnlyField(source='post.post')
    class Meta:
        model = Comment
        fields = (
            'id', 'user', 'post', 'comment', 'created_at', 
            'username', 'postname',
        )
        read_only_fields = ('created_at', 'user', )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('id', 'post', 'raiting', 'user', 'comments')
        read_only_fields = ('user', )


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = (
            'id', 'username', 'is_active', 'email', 
            'first_name', 'last_name', 'phone_number',
            'is_staff', 'posts',
        )
