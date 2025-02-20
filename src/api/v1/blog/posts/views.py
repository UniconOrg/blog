# views.py

from rest_framework import viewsets

from utils.auth import (
    SwaggerAutoSchemaMeta,
    SwaggerAutoSchemaViewSetMixin,
)

from .models import Posts
from .serializers import PostsSerializer


class PostsModelViewSet(
    SwaggerAutoSchemaViewSetMixin,
    viewsets.ModelViewSet,
    metaclass=SwaggerAutoSchemaMeta,
):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    tag = "Posts"

