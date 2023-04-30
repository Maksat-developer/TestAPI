from .models import (
    Menu,
    Comment,
    Recipe,
)

from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


menu_serializer = MenuSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


comment_serializer = CommentSerializer


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


recipe_serializer = RecipeSerializer
