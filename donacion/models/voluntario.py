from django.db import models
from donacion.base.perfil import Perfil
from donacion.base.types import TipoVoluntario


class Voluntario(Perfil):
    tipo_voluntario = models.CharField(choices=TipoVoluntario.choices, max_length=2)
