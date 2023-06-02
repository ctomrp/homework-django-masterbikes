from django.shortcuts import render, redirect
from django.contrib import messages
from models.models import Cliente
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    return(render(request,'login.html'))
def register(request):
    return(render(request,'register.html'))
def index(request):
    return(render(request,'index.html'))
def guardarregistro(request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        objCliente = Cliente.objects.create(
            user_name = username,
            email = email,
            password = password
        )
        objCliente.save()
        return(render(request,'login.html'))
            #context = {
           #     messages.error(request, 'Error, no se ingreso validamente')
           # }
           # return (render(request,context={'messages': messages.get_messages(request)})), redirect('register')