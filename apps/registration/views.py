from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

from .models import Profile
from .forms import RegisterForm, ProfileForm

class RegisterUser(CreateView):
    model = Profile
    form_class = RegisterForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class ProfileDetail(DetailView):
    model = Profile
    template_name = "registration/profile.html"

class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy('receta:index_receta')
