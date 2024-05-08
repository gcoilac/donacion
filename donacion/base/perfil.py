from django.db import models
from django.contrib.auth.models import User

from donacion.base.attrib import NULLABLE, DEFAULT_CHAR
from donacion.base.base_model import BaseModel
from django.db.models.signals import post_save
from donacion.base.types import tipoUser


class Perfil(BaseModel):
    nombre = models.CharField(**DEFAULT_CHAR)
    paterno = models.CharField(**DEFAULT_CHAR)
    materno = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    telefono = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    image = models.ImageField(default='users/descarga.png', upload_to='users/', **NULLABLE)
    tipo = models.CharField(choices=tipoUser.choices, max_length=2, default='Pendiente')
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.nombre + " " + self.paterno + " " + self.materno

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Perfil.objects.create(user=instance)

# def save_user_profile(sender, instance, **kwargs):
#     instance.perfil.save()

# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)