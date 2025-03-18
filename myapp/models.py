from django.db import models

# Create your models here.
class Projecto(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Creacion de modelos para la base de datos

class Task(models.Model):
    def __str__(self):
        return self.title + " - " + self.project.name
    done = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Projecto, on_delete=models.CASCADE)