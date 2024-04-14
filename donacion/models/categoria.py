from django.db import models

from donacion.base import DEFAULT_CHAR
from donacion.base.base_model import BaseModel


class Categoria(BaseModel):
    name = models.CharField(**DEFAULT_CHAR)
