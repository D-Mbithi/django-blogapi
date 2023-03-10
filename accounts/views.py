from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import UserProfileSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """User API List"""
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer


