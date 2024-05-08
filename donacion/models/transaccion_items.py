from django.db import models
from donacion.base.attrib import NULLABLE, DEFAULT_CHAR
from donacion.base.base_model import BaseModel
from donacion.models.transaccion import Transaccion
#from donacion.models.categoria import Categoria
from donacion.base.types import TipoDonacion
from donacion.models.producto import Producto
from donacion.models.alimento import Alimento
from donacion.models.bisuteria import Bisuteria
from donacion.models.economica import Economica


class TransaccionItems(BaseModel):
    nombre = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    cantidad = models.IntegerField()
    descripcion = models.TextField(**NULLABLE)
    categoria = models.CharField(choices=TipoDonacion.choices, max_length=2, **NULLABLE)
    datecompleted = models.DateTimeField(**NULLABLE)
    product = models.ForeignKey(Producto, on_delete=models.PROTECT, **NULLABLE, related_name="products")
    food = models.ForeignKey(Alimento, on_delete=models.PROTECT, **NULLABLE, related_name="foods")
    money = models.ForeignKey(Economica, on_delete=models.PROTECT, **NULLABLE, related_name="money")
    bisutery = models.ForeignKey(Bisuteria, on_delete=models.PROTECT, **NULLABLE, related_name="bisuterys")
    transaccion = models.ForeignKey(
        Transaccion, **NULLABLE, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.nombre