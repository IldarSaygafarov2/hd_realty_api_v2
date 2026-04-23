from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Category, PropertyType, RenovationType


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ["name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["created_at"]
    search_fields = ["name"]


@admin.register(RenovationType)
class RenovationTypeAdmin(ModelAdmin):
    list_display = ["title", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(PropertyType)
class PropertyTypeAdmin(ModelAdmin):
    list_display = ["name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["created_at"]
    search_fields = ["name"]
