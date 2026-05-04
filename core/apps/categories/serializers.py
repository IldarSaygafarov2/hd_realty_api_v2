from rest_framework import serializers
from .models import Category, RenovationType, PropertyType


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "created_at", "updated_at"]


class RenovationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenovationType
        fields = ["id", "title", "slug", "created_at", "updated_at"]


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ["id", "name", "slug", "created_at", "updated_at"]
