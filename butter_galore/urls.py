from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("foods/", include("meal.urls")),
    path("", include("about_us.urls")),
]
