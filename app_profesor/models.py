from django.db import models

# Create your models here.
# clase Profesor con los campos nombre, edad y email
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.email}"