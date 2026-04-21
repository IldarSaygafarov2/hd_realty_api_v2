from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import District


@admin.register(District)
class DistrictAdmin(ModelAdmin):
    list_display = ["name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    list_filter = ["created_at"]
