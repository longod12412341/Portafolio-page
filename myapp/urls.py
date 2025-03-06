
from django.urls import path
from . import views



urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("hello/<str:username>", views.hello),
    path("task/<int:id>", views.task),
    path("project/", views.projects),
]
