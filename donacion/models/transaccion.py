from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from donacion.base import NULLABLE
from donacion.base.base_model import BaseModel
from donacion.models.organizacion import Organizacion
from donacion.models.persona_natural import PersonaNatural
from donacion.models.voluntario import Voluntario


class EstadoTransaccion(models.TextChoices):
    REGISTRADO = "1", "Registrado"
    RECOLECTADO = "2", "Recolectado"
    SOLICITADO = "3", "Solicitado"
    DESPACHADO = "4", "Despachado"
    RECEPCIONADO = "5", "Recepcionado"


class Transaccion(BaseModel):
    donador_persona = models.ForeignKey(
        PersonaNatural,
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name="transaccion_donador"
    )
    receptor_persona = models.ForeignKey(
        PersonaNatural,
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name="transaccion_receptor"
    )
    donador_organizacion = models.ForeignKey(
        Organizacion,
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name="transaccion_donador"
    )
    receptor_organizacion = models.ForeignKey(
        Organizacion,
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name="transaccion_receptor"
    )

    recolectado_por = models.ForeignKey(
        Voluntario,
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name="transaccion_recolectado"
    )
    despachado_por = models.ForeignKey(
        Voluntario,
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name="transaccion_despachado"
    )
    fecha_registro = models.DateTimeField()
    fecha_envio = models.DateTimeField(**NULLABLE)
    fecha_recepcion = models.DateTimeField(**NULLABLE)
    estado = models.CharField(choices=EstadoTransaccion.choices, max_length=2)
