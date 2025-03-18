from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Projecto , Task
from django.shortcuts import get_object_or_404 , render, redirect
from .forms import CreateNewTask, CreateNewProjects
# Create your views here.

def about(request):
    username = "longo"
    return render(request, "about.html", {
        "username" : username
    })

def index(request):
    title = "Django Curso!!"
    return render(request, "index.html",{
        "title" : title
    })


def task(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html",{
        "tasks" : tasks 
    })
    
    
def projects(request):
    projects = Projecto.objects.all()
    return render(request, "projects/projects.html", {
        "projects" : projects
    })

def create_task(request) :
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {
            "form" : CreateNewTask()
        }) 
    else:
        Task.objects.create(title=request.POST["title"],
        description=request.POST["description"], project_id=2)
        return redirect("task")


def Create_projects(request):
    if request.method == "GET":
        return render(request, "projects/create_projects.html",{
            "form": CreateNewProjects()
        })
    else: 
        Projecto.objects.create(name=request.POST["name"])
        redirect("projects")