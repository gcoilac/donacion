from django import forms
from .models import Voluntario, PersonaNatural, Organizacion, Producto, TransaccionItems, Transaccion

class PersonaNaturalForm(forms.ModelForm):
    
    class Meta:
        model = PersonaNatural
        fields = ["nombre", "paterno", "materno", "telefono", "tipo_funcion", "represento_org"]
        widgets = {
            "nombre":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe tu nombre",
                }
            ), 
            "paterno":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe tu apellido paterno",
                }
            ), 
            "materno":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe tu apellido materno",
                }
            ), 
            "telefono":forms.NumberInput(attrs={'class': 'form-control'}),
            "tipo_funcion":forms.Select(attrs={'class': 'form-control'}),
            "Represento organizacion": forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }
        #fields = '__all__'


class VoluntarioForm(forms.ModelForm):
    
    class Meta:
        model = Voluntario
        fields = ["nombre", "paterno", "materno", "telefono", "tipo_voluntario"]
        widgets = {
            "nombre":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escriba tu nombre",
                }
            ), 
            "paterno":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe tu apellido paterno",
                }
            ), 
            "materno":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe tu apellido materno",
                }
            ),
            "tipo_voluntario":forms.Select(attrs={'class': 'form-control'}), 
            "telefono":forms.NumberInput(attrs={'class': 'form-control'})
        }
        #fields = '__all__'


class OrganizacionForm(forms.ModelForm):
    
    class Meta:
        model = Organizacion
        fields = ["razon_social", "telefono"]
        widgets = {
            "razon_social":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escriba un nombre de la organizacion",
                }
            ),
            "telefono":forms.NumberInput(attrs={'class': 'form-control'})
        }
        #fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["marca", "peso", "caducidad", "descripcion", "image"]
        widgets = {
            "marca": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "escriba el nombre de la empresa del producto",
                }
            ),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            "caducidad": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "escriba una descripcion",
                }
            ),
            #'asignacion': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
            #sender = forms.EmailField(help_text="A valid email address, please.")
            #day = forms.DateField(initial=datetime.date.today)
        }


class DonationForm(forms.ModelForm):
    class Meta:
        model = TransaccionItems
        fields = ["nombre", "cantidad", "categoria"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escriba un nombre de la donacion",
                }
            ),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            "categoria":forms.Select(attrs={'class': 'form-control'}), 
        }

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        #fields = '__all__'
        fields = ["fecha_registro", "fecha_envio", "fecha_recepcion", "estado"]
        widgets = {
            "fecha_registro": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            'fecha_envio': forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "fecha_recepcion": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "estado":forms.Select(attrs={'class': 'form-control'}), 
        }

# class PerfilForm(forms.ModelForm):
    
#     class Meta:
#         abstract = True
#         model = perfil
#         fields = ["nombre", "paterno", "materno", "telefono", "status"]
        # widgets = {
        #     "nombre":forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Escriba un nombre del producto",
        #         }
        #     ), 
        #     "paterno":forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Escriba un nombre del producto",
        #         }
        #     ), 
        #     "materno":forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Escriba un nombre del producto",
        #         }
        #     ), 
            #"telefono":forms.NumberInput(attrs={'class': 'form-control'}), 
            #"status":
        #}



        # model = Donacion
        # fields = ["nombre", "cantidad", "tipo"]
        # CHOICES = (
        #     ("1", "producto"),
        #     ("2", "alimento"),
        #     ("2", "economica"),
        #     ("2", "bisuteria"),
        # )
        # widgets = {
        #     "nombre": forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Escriba un nombre del producto",
        #         }
        #     ),
        #     'cantidad': forms.IntegerField(attrs={'class': 'form-control'}),
        #     "tipo": forms.Select(choices=CHOICES),
        # }


