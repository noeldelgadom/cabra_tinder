from django.db import models

# Create your models here.
class Goat(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    description = models.TextField()
    profile_pic = models.ImageField(upload_to="")
    pastor = models.CharField(max_length=128)

    def __str__(self):
        return self.name
