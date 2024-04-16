from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("foods/", include("meal.urls")),
    path("", include("about_us.urls")),
]
