from django import forms
from .models import Categories

class CategoriesFrom(forms.ModelForm):
    class Meta:
        model= Categories
        fields='__all__'