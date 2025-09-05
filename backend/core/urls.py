from django.urls import path
from . import views

urlpatterns = [
    path("api/health/", views.health_check, name="health-check"),
]
