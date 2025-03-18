
from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("task/", views.task, name="task"),
    path("project/", views.projects, name="projects"),
    path("create_task/", views.create_task, name="create_task"),
    path("create_projects/", views.Create_projects, name="create_projects"),
]
