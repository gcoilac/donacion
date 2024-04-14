from django.db import models
from donacion.base import DEFAULT_CHAR, NULLABLE
from donacion.base.base_model import BaseModel
from donacion.models.categoria import Categoria


class Producto(BaseModel):
    nombre = models.CharField(**DEFAULT_CHAR)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, **NULLABLE)
    image = models.ImageField(upload_to="images/", **NULLABLE)

    def __str__(self):
        return self.nombre
