from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=15,min_length=2)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
    
    #def clean_username(self):
    #    username = self.cleaned_data['username']
    #    return validate_username(username)
    #def clean_name(self):
    #    cleaned_data = super().clean()
    #    username1 = cleaned_data.get['username']
    #    existe = User.objects.filter(username=username1).exists()
    #   if existe:
    #       raise ValidationError('Este nombre ya existe')        
#def validate_username(username):
#        if User.objects.filter(username=username).exists():
#            raise forms.ValidationError("El nombre de usuario ya está en uso.")
#        if any(char.isdigit() for char in username):
#            raise forms.ValidationError("El nombre de usuario no puede contener números.")
#        return username


            
            
         
