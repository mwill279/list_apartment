from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="index"),
    path("contact/", views.contact, name="contact"),
]