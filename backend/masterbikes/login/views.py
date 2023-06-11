from django.shortcuts import render, redirect
from django.contrib import messages
from models.models import Cliente, TipoBicicleta, FormaPago, Arriendo, Bicicleta, ArriendoBicicleta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

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
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request,"Registro añadido correctamente!")
#   En caso de querer logear instantaneamente al usuario. 
# Se puede utilizar el siguiente codigo, borrando la linea de arriba y usando las dos de abajo. 
#Almacena el formulario que hiciste en un objeto y lo pasa con la funcion login para ingresarte automaticamente
            #user = User.objects.create_user(username=username, email=email, password=password)
            #login(request, user)
            return(render(request,'register.html'))
    else:
        form = RegistrationForm()
    return(render(request,'register.html'))

def index(request):
    return(render(request,'index.html'))

def exit(request):
    logout(request)
    return redirect('auth_login')

def recover_password(request):
    if  request.method == 'GET':       
        return(render(request,'recover_password.html'))
    





# Bastian...
    
@login_required
def formularioarriendo(request):

    objBici1 = Bicicleta.objects.raw('select * from models_bicicleta where tipo_bicicleta_id = 1;')
    objBici2 = Bicicleta.objects.raw('select * from models_bicicleta where tipo_bicicleta_id = 2;')
    objBici3 = Bicicleta.objects.raw('select * from models_bicicleta where tipo_bicicleta_id = 3;')

    #objBici1 = Bicicleta.objects.all()

    diccionario = {
        'tipo1' : objBici1,
        'tipo2' : objBici2,
        'tipo3' : objBici3
    }

    return(render(request,'formularioarriendo.html', diccionario))

def guardado(request):
    print('--> Ajajá esto saldrá en la consola donde está corriendo el server de Django...')

    if request.method == 'POST':
        print('Bien!! Es POST!!')


        bicis = request.POST["listaBicis"]
        garantia = request.POST['garantia']
        formaPago = request.POST['formaPago']
        inicio = request.POST['fechaInicio']
        fin = request.POST['fechaFin']

        print(bicis)
        print("--> bicis cortadas...")
        bicis = bicis.split(sep=',')
        bicis.pop()
        print(bicis)
        print("autenticado??...")
        print(request.user.is_authenticated)
        print("username: " + request.user.username)
        print("id...")
        print(request.user.id)
        
                
        objPago = FormaPago.objects.get(id = formaPago)
        objCliente = User.objects.get(id = request.user.id)

        objArr = Arriendo.objects.create(
            deposito_garantia = garantia,
            cliente = objCliente,
            forma_pago = objPago,
            fecha_inicio = inicio,
            fecha_termino = fin
        )
        objArr.save()

        print("---> Id del arriendo...")
        print(objArr.pk)

        largo = len(bicis)
        print("---> largo...")
        print(largo)
        for i in bicis:

            print("--> i...")
            print(i)
            objBici = Bicicleta.objects.get(id = i)
            objArrBic = ArriendoBicicleta.objects.create(
                arriendo = objArr,
                bicicleta = objBici
            )

            objArrBic.save()

    return render(request, 'guardado.html')