from django.db import models

# Create your models here.
class Goat(models.Model):
    nombre = models.CharField(max_length=128)
    diagnostico = models.CharField(max_length=128)
    sexo = models.CharField(max_length=128)
    edad = models.PositiveIntegerField()
    sexy_quote = models.TextField()
    profile_pic = models.CharField(max_length=300)
    pastor = models.CharField(max_length=128)
    raza = models.CharField(max_length=128)

    def __str__(self):
        return self.name
