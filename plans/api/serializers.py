from rest_framework import serializers

from plans.models import Plan, Recipe, Tag
from users.api.serializers import ProfileSerializer


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