from django.urls import path
from .views import auth_login, auth_register,index, formularioArriendo, exit, recover_password

# Bastian...
from .views import guardado

urlpatterns = [
    path('', index,name='index'),
    path('auth_login',auth_login,name='auth_login'),
    path('auth_register', auth_register,name='auth_register'),
    path('recover_password',recover_password,name='recover_password'),
    path('formularioarriendo',formularioArriendo,name='formularioArriendo'),
    path('logout',exit,name='exit'),



    # Bastian...
    path('guardado', guardado, name='guardado')


]