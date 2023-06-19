from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createconference", views.createconference, name="createconference")
]