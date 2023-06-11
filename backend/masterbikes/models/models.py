from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,EmailValidator
# Create your models here.
class TipoReparacion(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return str(self.name)
    
class TipoBicicleta(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return str(self.name)

class FormaPago(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return str(self.name)

class Cliente(models.Model):
    
    user_name = models.CharField(max_length=45, blank=False, null=False)
    email = models.EmailField(max_length=45, blank=False, null=False)
    password = models.CharField(max_length=45, blank=False, null=False)
 
    def __str__(self):
        return str(self.user_name)
    
class Reparacion(models.Model):
    fecha_reparacion = models.DateTimeField(max_length=45, blank=False, null=False)
    reparable = models.BooleanField(null=True)
    descripcion = models.TextField()
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    tipo_reparacion = models.ForeignKey('TipoReparacion',on_delete=models.CASCADE)

    def __str__(self):
        msn = f"{self.cliente} {self.tipo_reparacion}"
        return str(msn)
    
class Arriendo(models.Model):
    fecha_inicio = models.DateTimeField(max_length=45, null=False)
    fecha_termino = models.DateTimeField(max_length=45, null=True)
    deposito_garantia = models.IntegerField(null=False)
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    forma_pago = models.ForeignKey('FormaPago',on_delete=models.CASCADE)

    def __str__(self):
        msn = f"{self.cliente} {self.forma_pago}"
        return str(msn)
    
class Bicicleta(models.Model):
    color = models.CharField(max_length=45, blank=False, null=False)
    tamano_aro = models.IntegerField(null=False)
    tipo_bicicleta = models.ForeignKey('TipoBicicleta',on_delete=models.CASCADE)

    def __str__(self):
        msn = f"{self.tamano_aro} {self.tipo_bicicleta}"
        return str(msn)
    
class ArriendoBicicleta(models.Model):
    arriendo = models.ForeignKey('Arriendo',on_delete=models.CASCADE)
    bicicleta = models.ForeignKey('Bicicleta',on_delete=models.CASCADE)

    def __str__(self):
        msn = f"{self.arriendo} {self.bicicleta}"
        return str(msn)