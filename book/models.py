from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    sinopsys = models.TextField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre