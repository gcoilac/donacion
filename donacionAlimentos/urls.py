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
from django.urls import path
from donacion import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),


    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('edit/', views.edit, name='edit'),
    path('signin/', views.signin, name='signin'),
    path('password/', views.password, name='password'),
    path('emailsentconfirm/', views.emailsentconfirm, name='emailsentconfirm'),
    path("perfil/", views.perfil, name="perfil"),
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

    path('transaccion_items/', views.transaccion_items, name='transaccion_items'),
    path('productos/', views.products, name='products'),
    path('productos_donados/', views.donated_products, name='donated_products'),
    path('productos/cantidad/', views.cantidad_producto, name='cantidad_producto'),
    path('productos/subir/', views.subir_producto, name='subir_producto'),
    path('products/<int:product_id>/', views.detalle_Producto, name='detalle_Producto'),
    path('products/<int:product_id>/complete', views.entrega_producto, name='entrega_producto'),
    path('products/<int:product_id>/delete', views.borrar_producto, name='borrar_producto'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
