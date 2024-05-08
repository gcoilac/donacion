from django.db import models
from donacion.base.attrib import DEFAULT_CHAR, NULLABLE, DEFAULT_DECIMAL
from donacion.base.base_model import BaseModel



class Producto(BaseModel):
    marca = models.CharField(**DEFAULT_CHAR)
    peso = models.DecimalField(**DEFAULT_DECIMAL, **NULLABLE)
    caducidad = models.DateField(**NULLABLE)
    creacion = models.DateTimeField(auto_now_add=True, **NULLABLE)
    image = models.ImageField(upload_to="images/", **NULLABLE)

    def __str__(self):
        return self.marca
