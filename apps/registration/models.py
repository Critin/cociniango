from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Premio(models.Model):
    
    CATEGORY_CHOICES = [
        ("C", ("Premio Colaborador")),
        ("SP", ("Sin premio")),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=False, blank=False,  default="SP")

    def __str__ (self):
        return '{}'.format(self.category)

class Profile(models.Model):

    GENDER_CHOICES = [
        ("M", ("Masculino")),
        ("F", ("Femenino")),
        ("NE", ("No especificado")),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True, default="NE")
    age = models.IntegerField(null= True, blank=True)
    reward = models.ManyToManyField(Premio)

    def __str__(self):
        return '{}'.format(self.user.first_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
