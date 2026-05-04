from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from core.api.main import api_app
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # YOUR PATTERNS
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.apps.districts.urls")),
    path("api/", include("core.apps.categories.urls")),
    path("api/", include("core.apps.main.urls")),
    # path("api/", api_app.urls),
]

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
