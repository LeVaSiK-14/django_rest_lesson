from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    PostViewSet, 
    CommentViewSet,
    UserViewSet,
)

router = DR()

router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
router.register('users', UserViewSet, basename='users')

urlpatterns = []

urlpatterns += router.urls