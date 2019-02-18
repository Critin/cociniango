from django.shortcuts import render, redirect
import os
from apps.recetas.forms import RecetaForm
from apps.recetas.models import Receta, Comment, Authorship
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import CommentForm

class Index(TemplateView):
    template_name = "recetas/index.html"

# Filtro

def filtro(request):
    filtro = request.POST.get('filtro', '')
    object_list = Receta.objects.filter(name__icontains=filtro)
    return render(request, 'recetas/recetas_list.html', {'object_list':object_list})

# Función para añadir recetas

def addReceta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('receta:list_recetas')
    else:
        form = RecetaForm()

    return render(request, 'recetas/recetas_form.html', {'form':form})

# Listar recetas
class RecetasList(ListView):
    model = Receta
    template_name = 'recetas/recetas_list.html'

# Preparar receta
class RecetaDetail(DetailView):
    model = Receta
    template_name = 'recetas/receta_detail.html'

# Ver comentarios
class CommentList(ListView):
    model = Comment
    template_name = 'recetas/receta_detail.html'

# Añadir comentarios
class CommentCreate(CreateView):
    model = Comment
    template_name = 'recetas/add_comment.html'
    form_class = CommentForm

# Editar recetas
class RecetaUpdate(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = "recetas/receta_edit.html"
    success_url = reverse_lazy('receta:list_recetas')

# Eliminar recetas
class RecetaDelete(DeleteView):
    model = Receta
    template_name = "recetas/receta_delete.html"
    success_url = reverse_lazy('receta:list_recetas')
