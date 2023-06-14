from django.urls import path
from .views import auth_login, auth_register,index, formularioarriendo, exit, recover_password, repair_form

# Bastian...
from .views import guardado

urlpatterns = [
    path('', index,name='index'),
    path('auth_login',auth_login,name='auth_login'),
    path('auth_register', auth_register,name='auth_register'),
    path('recover_password',recover_password,name='recover_password'),
    path('formularioarriendo',formularioarriendo,name='formularioarriendo'),
    path('repair_form',repair_form,name='repair_form'),
    path('logout',exit,name='exit'),



    # Bastian...
    path('guardado', guardado, name='guardado')


]