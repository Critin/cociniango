from django import forms

from apps.recetas.models import Receta, Comment

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta

        fields = [
            'name',
            'description',
            'ingredients',
            'instructions',
            'plate',
            'image',
            'author',
        ]

        labels = {
            'name': 'Nombre de la receta',
            'description': 'Descripción',
            'ingredients': 'Ingredientes',
            'instructions': 'Cómo preparar',
            'plate': 'Plato',
            'image': 'Imagen',
            'author': 'Autoría',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'ingredients': forms.Textarea(attrs={'class':'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'plate': forms.Select(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(),
            'author': forms.Select(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'content',
            'image',
        ]