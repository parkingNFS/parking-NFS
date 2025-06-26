from django.db import models
class usuarios (models.model):
    nombre=models.TextField ("nombre")
    apellido=models.TextField ("apellido")
    rol_id=models.integerfield ("rol")
    