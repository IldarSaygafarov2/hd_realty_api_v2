from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view()),
    path("renovation-types/", views.RenovationTypeListView.as_view()),
    path("property-types/", views.PropertyTypeListView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
