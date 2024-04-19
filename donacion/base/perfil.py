from django.db import models
from django.contrib.auth.models import User

from donacion.base.attrib import NULLABLE, DEFAULT_CHAR
from donacion.base.base_model import BaseModel
from donacion.base.types import tipoUser


class Perfil(BaseModel):
    nombre = models.CharField(**DEFAULT_CHAR)
    paterno = models.CharField(**DEFAULT_CHAR)
    materno = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    telefono = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    status = models.IntegerField(**NULLABLE, choices=tipoUser)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __unicode__(self):
        return u'%s - %s ' %(self.nombre, self.paterno, self.materno, self.telefono, self.status, )

    # def __str__(self) -> str:
    #     return self.nombre + " " + self.paterno + " " + self.materno
