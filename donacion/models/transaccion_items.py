from django.db import models
from donacion.base import NULLABLE
from donacion.base.base_model import BaseModel
from donacion.models.producto import Producto
from donacion.models.transaccion import Transaccion


class TransaccionItems(BaseModel):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    transaccion = models.ForeignKey(
        Transaccion, on_delete=models.CASCADE, related_name="items"
    )
    cantidad = models.IntegerField()
    expiration_date = models.DateField(**NULLABLE)
