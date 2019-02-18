from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Receta(models.Model):
    
    TYPE_OF_PLATE_CHOICES = [
        ("Entrante", ("Primero")),
        ("Principal", ("Segundo")),
        ("Postre", ("Tercero")),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField(default="Esta receta no tiene instrucciones.")
    plate = models.CharField(max_length=20, choices=TYPE_OF_PLATE_CHOICES, blank=False)
    image = models.ImageField(upload_to='recetas', null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name, self.author.first_name)

class Authorship(models.Model):
    authors = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.authors.first_name)


class Comment(models.Model):

    receta = models.ForeignKey(Receta, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ManyToManyField(Authorship)
    content = models.TextField()
    image = models.ImageField(upload_to='comment', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.receta.name, self.content)
