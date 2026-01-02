from django import forms
from django.contrib.auth.models import User as Usuario

# Criando o formulário de login
class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            ),
        }
    

