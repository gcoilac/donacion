from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Alimento(models.Model):
    tipo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

class Donante(models.Model):
    ubicacion = models.CharField(max_length=100)

class Donacion(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    cantidad = models.IntegerField(null=True)
    tipo = models.CharField(max_length=100, blank=True)
    #frecuencia = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class OrgBeneficiaria(models.Model):
    razonsocial = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

class Producto(models.Model):
    empresa = models.CharField(max_length=100, blank=True)
    caducidad = models.DateField()
    descripcion = models.TextField(blank=True)
    image = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.empresa
    # def __str__(self):
    #     return self.nombre + ' - by ' + self.user.username

class Administrador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.usuario.nombre} (ID: {self.usuario.id})'

class Voluntario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    turno = models.CharField(max_length=100)
    tarea = models.CharField(max_length=100)
    responzable = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.usuario.username} (ID: {self.usuario.id})'

class Solicita(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    org_beneficiaria = models.ForeignKey(OrgBeneficiaria, on_delete=models.CASCADE)

class ResponsableOrg(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    org_benefica = models.ForeignKey(OrgBeneficiaria, on_delete=models.CASCADE)
    cargo = models.IntegerField()
    def __str__(self):
        return f'{self.usuario.username} (ID: {self.usuario.id})'

class Requiere(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    org_beneficiaria = models.ForeignKey(OrgBeneficiaria, on_delete=models.CASCADE)

class Realiza(models.Model):
    donacion = models.ForeignKey(Donacion, on_delete=models.CASCADE)
    donante = models.ForeignKey(Donante, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    fecha = models.DateTimeField()

class Proporciona(models.Model):
    org_beneficiaria = models.ForeignKey(OrgBeneficiaria, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=True, blank=True)
    asignacion = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.voluntario.username} (ID: {self.voluntario.id})'

class PersonaDonante(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesion = models.ForeignKey(Donante, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.usuario.username} (ID: {self.usuario.id})'

class Perfil(models.Model):
    apellidoP = models.CharField(max_length=100)
    apellidoM = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)
    etiqueta = models.CharField(max_length=100)
    bibliografia = models.TextField()
    sitio_web = models.URLField()
    foto = models.ImageField(upload_to="perfiles", null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.usuario.username} (ID: {self.usuario.id})'

class Participa(models.Model):
    donacion = models.ForeignKey(Donacion, on_delete=models.CASCADE)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)

class OrgDonante(models.Model):
    razon_social = models.CharField(max_length=100)
    area_servicio = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)
    sitio_web = models.URLField()
    donante = models.ForeignKey(Donante, on_delete=models.CASCADE)

class Alerta(models.Model):
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    donacion = models.ForeignKey(Donacion, on_delete=models.CASCADE)

class Notifica(models.Model):
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.usuario.username} (ID: {self.usuario.id})'
    
class Entrega(models.Model):
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    org_beneficiaria = models.ForeignKey(OrgBeneficiaria, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

class Dispone(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    donacion = models.ForeignKey(Donacion, on_delete=models.CASCADE)
    duracion_aprox = models.CharField(max_length=100)

class Cataloga(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    donacion = models.ForeignKey(Donacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now, blank=True)
    disponibilidad = models.BooleanField(default=False)

