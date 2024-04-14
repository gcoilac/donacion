from django.db import models
from django.contrib.auth.models import User

from donacion.base import NULLABLE, DEFAULT_CHAR
from donacion.base.base_model import BaseModel


class Perfil(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nombre = models.CharField(**DEFAULT_CHAR)
    paterno = models.CharField(**DEFAULT_CHAR)
    materno = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    telefono = models.CharField(**DEFAULT_CHAR, **NULLABLE)

    class Meta:
        abstract = True

    # def __str__(self) -> str:
    #     return self.nombre + " " + self.paterno + " " + self.materno
