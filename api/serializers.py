from rest_framework import serializers

from users.models import Profile
from plans.models import Plan, Recipe, Tag


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False)
    favourites = ProfileSerializer(many=True)
    tag = TagSerializer(many=True)
    class Meta:
        model = Recipe
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    personal_plan = ProfileSerializer(many=False)
    recipes = RecipeSerializer(many=True)
    tag = TagSerializer(many=True)
    class Meta:
        model = Plan
        fields = '__all__'