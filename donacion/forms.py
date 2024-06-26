from django import forms
from .models import Producto, Donacion

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields =  ['empresa', 'caducidad', 'descripcion', 'image']
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escriba el nombre de la empresa del producto'}),
            'caducidad': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'escriba una descripcion'}), 
            
            #'asignacion': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
            #sender = forms.EmailField(help_text="A valid email address, please.")
            #day = forms.DateField(initial=datetime.date.today)
        }
    
class DonationForm(forms.ModelForm):
        class Meta:
            model = Donacion
            fields = ['nombre', 'cantidad', 'tipo']
            CHOICES = (('1','producto'), ('2','alimento'), ('2','economica'), ('2','bisuteria'),)
            widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un nombre del producto'}),
                #'cantidad': forms.IntegerField(attrs={'class': 'form-control'}),
                'tipo': forms.Select(choices=CHOICES),
            }