from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shifts/", include("shifts_planner.urls", namespace="shifts")),
]
