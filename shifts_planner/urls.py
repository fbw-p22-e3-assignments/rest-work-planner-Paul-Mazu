from django.urls import path
from . import views

app_name = "shifts"
urlpatterns = [
    path("", views.ShiftsListApiView.as_view(), name="shifts"),
    path("<int:pk>/", views.ShiftDetailApiView.as_view(), name="shifts_detail"),
]
