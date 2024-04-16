from django.urls import path
from . import views

urlpatterns = [
    path("all-items/", views.all_items, name="all-items"),
]
