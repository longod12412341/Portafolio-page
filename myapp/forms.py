from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea)
    
    
class CreateNewProjects(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200)