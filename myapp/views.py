from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Projecto , Task
from django.shortcuts import get_object_or_404 , render
# Create your views here.

# Podemos concatenar nombres, numero e id 
def hello(request, username): #En vez de usar username usamos id pero debemos cambiar el 
    #el str de las urls a int, siempre debemos saber que tipo de datos le vamos a dar
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" % username)

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


def task(request, id):
    get_object_or_404(Task, id=id)
    return render(request, "tasks.html")
    return HttpResponse("<h1>Tasks : %</h1>" % task.title )
    
def projects(request):
    return render(request, "projects.html")
    projects = list(Projecto.objects.values())
    return JsonResponse(projects, safe=False) 
    
    