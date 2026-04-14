from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget

from .models import (
    FAQ,
    ConsultingRequest,
    Portfolio,
    Service,
    ServiceInclude,
    JobsChoices,
)


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    list_filter = ["created_at"]


@admin.register(ConsultingRequest)
class ConsultingRequestAdmin(ModelAdmin):
    list_display = ["name", "phone_number", "goal", "created_at"]
    list_display_links = ["name"]
    list_filter = ["goal", "created_at"]


class ServiceIncludeInline(admin.TabularInline):
    model = ServiceInclude
    extra = 1


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ["title", "deadlines", "format", "created_at"]
    list_filter = ["created_at"]
    inlines = [ServiceIncludeInline]
