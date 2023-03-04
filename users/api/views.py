from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from users.models import Profile
from .serializers import (ProfileSerializer, UserSerializer,)

# Profile views
class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [IsStaffEditorPermission]


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'pk'

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     if not instance.content:
    #         instance.content = instance.title