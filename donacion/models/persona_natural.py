from django.db import models

from donacion.base.attrib import NULLABLE
from donacion.base.perfil import Perfil
from donacion.base.types import TipoFuncion


class PersonaNatural(Perfil):
    tipo_funcion = models.CharField(choices=TipoFuncion.choices, max_length=2)
    represento_org = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.paterno} {self.materno}"
