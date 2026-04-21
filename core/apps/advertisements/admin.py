from django.contrib import admin

from unfold import admin as unfold_admin
from .models import Advertisement, AdvertisementImage, AdvertisementCharacterstic


class AdvertisementImageInline(unfold_admin.StackedInline):
    model = AdvertisementImage
    extra = 1


class AdvertisementCharacteristicInline(unfold_admin.StackedInline):
    model = AdvertisementCharacterstic
    extra = 1


@admin.register(Advertisement)
class AdvertisementAdmin(unfold_admin.ModelAdmin):
    list_display = [
        "title",
        "operation_type",
        "renovation_type",
        "category",
        "district",
        "created_at",
    ]
    inlines = [AdvertisementImageInline, AdvertisementCharacteristicInline]
    list_filter = [
        "category",
        "district",
        "operation_type",
        "renovation_type",
        "is_moderated",
        "created_at",
    ]
    list_editable = ["operation_type", "renovation_type", "category", "district"]
    search_fields = ["title"]
    readonly_fields = ["price_uzs"]
