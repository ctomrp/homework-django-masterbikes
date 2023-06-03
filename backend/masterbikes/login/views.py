from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.models import User


# Create your views here.
def auth_login(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message= 'Nombre de usuario o contraseña incorrecto'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return(render(request,'login.html'))
def auth_register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, email=email, password=password)
#   En caso de querer logear instantaneamente al usuario. 
#   Se puede utilizar el siguiente codigo, borrando la linea de arriba y usando las dos de abajo. 
#   Almacena el formulario que hiciste en un objeto y lo pasa con la funcion login para ingresarte automaticamente
            #user = User.objects.create_user(username=username, email=email, password=password)
            #login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('auth_login')
    else:
        form = RegistrationForm()
    return(render(request,'register.html'))
def index(request):
    return(render(request,'index.html'))

@login_required
def formularioArriendo(request):
    return(render(request,'formularioArriendo.html'))

def exit(request):
    logout(request)
    return redirect('auth_login')