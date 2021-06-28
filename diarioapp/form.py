from django import forms
from .models import Diario

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput)

class DiarioForm(forms.ModelForm):
    class Meta:
        model = Diario
        fields = ('conteudo',)
