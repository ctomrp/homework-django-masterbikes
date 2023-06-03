from django.shortcuts import render, redirect
from django.contrib import messages
from models.models import Cliente
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
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
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