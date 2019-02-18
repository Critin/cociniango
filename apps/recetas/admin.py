from django.contrib import admin

from apps.recetas.models import Receta, Authorship, Comment

# Register your models here.
admin.site.register(Receta)
admin.site.register(Authorship)
admin.site.register(Comment)