from django.db import models

# from django.core.mail import send_mail
# from django.shortcuts import render
# from django.conf import settings
# from models.models import *
# Create your models here.

# def enviar_correo(request):
#     if request.method == 'POST':
#         username = request.POST.get('user_name', '')
#         email = request.POST.get('email', '')

#         # Lógica para enviar el correo electrónico
#         subject = '¡Hola, {}'.format(username)
#         message = 'Este es un correo de prueba enviado a {}'.format(correo)
#         remitente = settings.EMAIL_HOST_USER
#         destinatarios = [email]

#         send_mail(subject, message, remitente, destinatarios)

#         # Renderizar la plantilla de confirmación de envío de correo
#         return render(request, 'recover_password.html', {'nombre_usuario': username})

#     return render(request, 'recover_password.html')