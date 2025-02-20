# serializers.py
from rest_framework import serializers

from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class WebHookSerializer(serializers.Serializer):
    pass
