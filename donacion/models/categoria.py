from django.db import models

from donacion.base.attrib import NULLABLE
from donacion.base.base_model import BaseModel
from donacion.base.types import TipoDonacion


class Categoria(BaseModel):
    tipo_donacion = models.CharField(choices=TipoDonacion.choices, max_length=2, **NULLABLE)
