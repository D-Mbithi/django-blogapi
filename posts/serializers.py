from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    """Post model serializer."""

    class Meta:
        fields = [
            "id",
            "author",
            "title",
            "body",
            "created"
        ]
        model = Post
