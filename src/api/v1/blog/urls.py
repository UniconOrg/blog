# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .posts.views import PostsModelViewSet

router = DefaultRouter()

router.register(r"posts/crud", PostsModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
