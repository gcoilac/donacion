from django.db import models
from donacion.base.attrib import NULLABLE, DEFAULT_CHAR
from donacion.base.base_model import BaseModel
from donacion.models.transaccion import Transaccion
#from donacion.models.categoria import Categoria
from donacion.base.types import TipoDonacion


class TransaccionItems(BaseModel):
    nombre = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    cantidad = models.IntegerField()
    categoria = models.CharField(choices=TipoDonacion.choices, max_length=2, **NULLABLE)
    datecompleted = models.DateTimeField(**NULLABLE)
    transaccion = models.ForeignKey(
        Transaccion, **NULLABLE, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.nombre