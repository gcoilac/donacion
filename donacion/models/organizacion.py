from django.db import models


from donacion.base.attrib import DEFAULT_CHAR, NULLABLE
from donacion.base.base_model import BaseModel
from .persona_natural import PersonaNatural


class Organizacion(BaseModel):
    responsable = models.ForeignKey(
        PersonaNatural, on_delete=models.SET_NULL, **NULLABLE
    )
    razon_social = models.CharField(**DEFAULT_CHAR)
    telefono = models.CharField(**DEFAULT_CHAR)

    def __str__(self) -> str:
        return self.razon_social
