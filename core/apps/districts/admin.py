from django.contrib import admin

from .models import District


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
    list_filter = ["created_at"]
