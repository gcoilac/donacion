from django.db import models


class TipoVoluntario(models.TextChoices):
    RESPONSABLE = "R", "Responsable"
    COLABORADOR = "C", "Colaborador"


class TipoFuncion(models.TextChoices):
    DONANTE = "D", "Donante"
    RECEPTOR = "R", "Receptor"

class TipoMoneda(models.TextChoices):
    BOLIVIANOS = "B", "Bs"
    DOLARES = "D", "$"


class tipoUser(models.TextChoices):
    VOLUNTARIO_RESPONZABLE = "VR", "Voluntario Responzable"
    VOLUNTARIO_COLABORADOR = "VC", "Voluntario Colaborador"
    DONANTE = "DP", "Donante"
    DONANTE_ORGANIZACION = "DO", "Donante Organizacion"
    RECEPTOR = "R", "Receptor"

class TipoDonacion(models.TextChoices):
    PRODUCTO = "P", "Producto"
    ALIMENTO = "A", "Alimento"
    VISUTERIA = "B", "Bisuteria"
    ECONOMIA = "E", "Economica"