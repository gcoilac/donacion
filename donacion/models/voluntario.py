from django.db import models
from donacion.base.attrib import NULLABLE
from donacion.base.perfil import Perfil
from donacion.base.types import TipoVoluntario


class Voluntario(Perfil):
    tipo_voluntario = models.CharField(choices=TipoVoluntario.choices, max_length=2)
    supervisor = models.ForeignKey(
        "self", **NULLABLE, related_name="colaboradores", on_delete=models.SET_NULL
    )   

    def __str__(self) -> str:
        return f"{self.nombre} {self.paterno}"
