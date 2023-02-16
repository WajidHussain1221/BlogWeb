from django.urls import path
from . import  views
urlpatterns = [
    path("", views.index),
    path("downloads/<int:id>", views.downloads)
]