from rest_framework import generics

from .models import Category, RenovationType, PropertyType
from .serializers import (
    CategorySerializer,
    PropertyTypeSerializer,
    RenovationTypeSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RenovationTypeListView(generics.ListAPIView):
    queryset = RenovationType.objects.all()
    serializer_class = RenovationTypeSerializer


class PropertyTypeListView(generics.ListAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
