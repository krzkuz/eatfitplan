from rest_framework import generics
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404

from users.models import Profile

from .serializers import ProfileSerializer, TagSerializer, RecipeSerializer, PlanSerializer
from plans.models import Plan, Recipe, Tag


# Profile views
class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileListAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# Plan views
class PlanListAPIView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# Recipe views
class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# Plan views
class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
