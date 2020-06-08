from django.urls import path
from rest_framework import routers
from . import views


urlpatterns = [
    path("projects/",views.Projects.as_view())
]




