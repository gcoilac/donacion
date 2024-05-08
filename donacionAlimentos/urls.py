"""
URL configuration for donacionAlimentos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from donacion import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),

    path("admin/", admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),

    path('mensaje/', views.mensaje, name='mensaje'),

    path("perfil/<str:username>/", views.perfil, name="perfil"),
    path("perfil/<int:user_id>/edit", views.edit_perfil, name="edit_perfil"),

    path("tipo_usuario/", views.tipo_usuario, name="tipo_usuario"),
    path("solicitud/", views.solicitud, name="solicitud"),
    path("solicitudVoluntario/", views.solicitudVoluntario, name="solicitudVoluntario"),
    path("solicitudPersona/", views.solicitudPersona, name="solicitudPersona"),
    path("solicitudOrganizacion/", views.solicitudOrganizacion, name="solicitudOrganizacion"),

    path('about/', views.about, name='about'),
    path('collect/', views.collect, name='collect'),
    path('contact/', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path('donationdetails/', views.donationdetails, name='donationdetails'),
    path('food/', views.food, name='food'),
    path('money/', views.money, name='money'),
    path('question/', views.question, name='question'),
    path('services/', views.services, name='services'),
    path('sampleinnerpage/', views.sampleinnerpage, name='sampleinnerpage'),


    path('donaciones/', views.donaciones, name='donaciones'),
    path('donaciones_donados/', views.cantidad_donaciones, name='donaciones_donados'),
    path('donaciones/cantidad/', views.cantidad_donaciones, name='cantidad_donaciones'),


    path('productos/subir/', views.subir_producto, name='subir_producto'),
    path('products/<int:product_id>/', views.detalle_producto, name='detalle_Producto'),
    path('products/<int:product_id>/complete', views.entrega_producto, name='entrega_producto'),
    path('products/<int:product_id>/delete', views.borrar_producto, name='borrar_producto'),


    path('alimentos/subir/', views.subir_alimento, name='subir_alimento'),
    # path('alimentos/<int:product_id>/', views.detalle_alimento, name='detalle_Producto'),
    # path('alimentos/<int:product_id>/complete', views.entrega_alimento, name='entrega_producto'),
    # path('alimentos/<int:product_id>/delete', views.borrar_alimento, name='borrar_producto'),


    path('bisuterias/subir/', views.subir_bisuteria, name='subir_bisuteria'),
    # path('bisuterias/<int:product_id>/', views.detalle_bisuteria, name='detalle_Producto'),
    # path('bisuterias/<int:product_id>/complete', views.entrega_producto, name='entrega_producto'),
    # path('bisuterias/<int:product_id>/delete', views.borrar_bisuteria, name='borrar_producto'),


    path('economica/subir/', views.subir_economica, name='subir_economica'),
    # path('economica/<int:product_id>/', views.detalle_economica, name='detalle_Producto'),
    # path('economica/<int:product_id>/complete', views.entrega_economica, name='entrega_producto'),
    # path('economica/<int:product_id>/delete', views.borrar_economica, name='borrar_producto'),


    path('transaccion/', views.transaccion, name='transaccion'),
    path('voluntario/', views.voluntario, name='voluntario'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
