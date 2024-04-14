from django.contrib import admin

from donacion.models.organizacion import Organizacion
from donacion.models.persona_natural import PersonaNatural
from donacion.models.voluntario import Voluntario

# from .models import (
#     Alimento, Donante, Producto, Donacion,  OrgBeneficiaria,
#     Administrador, Voluntario, Solicita, ResponsableOrg,
#     Requiere, Realiza, Proporciona, PersonaDonante, Perfil, Participa,
#     OrgDonante, Alerta, Notifica, Entrega, Dispone, Cataloga
# )


# Registra todos los modelos en el admin

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonaNatural)
class PersonaNaturalAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nombre",
        "paterno",
        "materno",
        "telefono",
        "tipo_funcion"
    )

@admin.register(Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    list_display = (
        "responsable",
        "razon_social",
        "telefono",
        "tipo_funcion",
    )

# admin.site.register(Alimento)
# admin.site.register(Donacion)
# admin.site.register(Donante)
# admin.site.register(OrgBeneficiaria)
# admin.site.register(Producto)

# admin.site.register(Administrador)
# admin.site.register(Voluntario)
# admin.site.register(Solicita)
# admin.site.register(ResponsableOrg)
# admin.site.register(Requiere)
# admin.site.register(Realiza)
# admin.site.register(Proporciona)
# admin.site.register(PersonaDonante)
# admin.site.register(Perfil)
# admin.site.register(Participa)
# admin.site.register(OrgDonante)
# admin.site.register(Alerta)
# admin.site.register(Notifica)
# admin.site.register(Entrega)
# admin.site.register(Dispone)
# admin.site.register(Cataloga)
