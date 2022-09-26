from rest_framework.viewsets import ModelViewSet
from mainapp.serializers import(
    Post, PostSerializer, 
    Comment, CommentSerializer,
)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    