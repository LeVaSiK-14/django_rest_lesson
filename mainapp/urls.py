from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    PostViewSet, 
    CommentViewSet
)

router = DR()

router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = []

urlpatterns += router.urls