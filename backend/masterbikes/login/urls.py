from django.urls import path
from .views import login, register, guardarregistro,index

urlpatterns = [
    path('', index,name='index'),
    path('login',login,name='login'),
    path('register', register,name='register'),
    path('guardarregistro', guardarregistro,name='guardarregistro'),

]