from django.db import models


class TipoVoluntario(models.TextChoices):
    RESPONSABLE = "R", "Responsable"
    COLABORADOR = "C", "Colaborador"


class TipoFuncion(models.TextChoices):
    DONANTE = "D", "Donante"
    RECEPTOR = "R", "Receptor"
