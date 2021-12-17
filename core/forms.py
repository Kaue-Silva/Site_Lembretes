from django.contrib.auth import forms
from django import forms
from .models import Lembrete


class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = ['titulo', 'descricao', 'data_hora']
        widgets = {
            'data_hora': forms.TextInput(attrs={'type':'datetime-local'})
        }
