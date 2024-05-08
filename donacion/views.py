from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Producto, TransaccionItems, Transaccion, Voluntario, PersonaNatural, Organizacion, Perfil
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PersonaNaturalForm, VoluntarioForm, OrganizacionForm, ProductForm, DonationForm, TransaccionForm, UserForm, AlimentoForm, BisuteriaForm, EconomicaForm
#from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import send_mail

# Create your views here.
def index(request):
    count_voluntario = Voluntario.objects.count()
    count_Transaccion = Transaccion.objects.count()
    PersonaNatural_receptora = PersonaNatural.objects.filter(tipo_funcion = 'Receptor')
    count_PersonaNatural_receptora = PersonaNatural_receptora.count()
    PersonaNatural_donante = PersonaNatural.objects.filter(tipo_funcion = 'Donante')
    count_PersonaNatural_donante = PersonaNatural_donante.count()
    return render(request, 'index.html', {
        'count_voluntario': count_voluntario,
        'count_Transaccion': count_Transaccion,
        'count_PersonaNatural_receptora': count_PersonaNatural_receptora,
        'count_PersonaNatural_donante': count_PersonaNatural_donante
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html', {
        'form': UserCreationForm
    })
    else:
            if request.POST['password1'] == request.POST['password2']:
                #register user
                try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('tipo_usuario')
                except IntegrityError:
                    return render(request, 'registration/signup.html', {
                        'form': UserCreationForm,
                        "error": 'User already exists'
                    })
    return render(request, 'registration/signup.html', {
    'form': UserCreationForm,
    "error": 'password do not match'
    })

def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username = request.POST['username'], password = request.POST['password']
        )
        if user is None:
            return render(request, 'registration/signin.html', {
                'form': AuthenticationForm,
                'error': 'username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('solicitud')

@login_required
def signout(request):
    logout(request)
    return redirect('index')


def perfil(request, username=None):
    user = User.objects.get(username=username)
    return render(request, 'registration/profile.html',{
        'user': user,
        'form': UserForm
    })   
    
@login_required
def edit_perfil(request, user_id):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)
        form = UserForm(instance=user)
        return render(request, 'registration/profile.html', {
            'product': user,
            'form': form
        })
    else:
        try:
            user = get_object_or_404(User, pk=user_id)
            form = UserForm(request.POST, instance=user)
            form.save()
        except ValueError:
            return render(request, 'registration/profile.html', {
            'product': user,
            'form': form,
            'error': 'Error updating product'
        })

def tipo_usuario(request):
    return render(request, 'registration/solicitude.html')

def solicitud(request):
    status = request.GET['status']
    if(status == '1'):
        return redirect('solicitudVoluntario')
    elif(status == '2'):
        return redirect('solicitudPersona')
                
@login_required
def solicitudVoluntario(request):
    if request.method == 'GET':
        return render(request, 'registration/voluntario.html', {
            'form': VoluntarioForm
        })
    else:
        try:
            if request.method == 'POST':
                form = VoluntarioForm(request.POST)
                if form.is_valid:
                    new_voluntario = form.save(commit=False)
                    new_voluntario.user = request.user
                    form.save()
                    return redirect('index')
        except ValueError:
            return render(request, 'registration/solicitude.html', {
                'form': VoluntarioForm(),           
                'error': 'please provide valude data'
            })
                
@login_required
def solicitudPersona(request):
    if request.method == 'GET':
            return render(request, 'registration/persona.html', {
            'form': PersonaNaturalForm()
        })
    else:
        try:
            if request.method == 'POST':
                form = PersonaNaturalForm(request.POST)
                if form.is_valid:
                    newform = form.save(commit=False)
                    newform.user = request.user
                    newform.save()
                    try:
                        represento_org = request.POST['represento_org']
                    except MultiValueDictKeyError:
                        represento_org = False
                    if represento_org:
                        return redirect('solicitudOrganizacion')
                    else:
                        return redirect('index')
        except ValueError:
            return render(request, 'registration/solicitude.html', {
                'form': PersonaNaturalForm(),           
                'error': 'please provide valude data'
            })
        
def solicitudOrganizacion(request):
    if request.method == 'GET':
        return render(request, "registration/organizacion.html", {
            'form': OrganizacionForm
        })
    else:
        try:
            if request.method == 'POST':
                form = OrganizacionForm(request.POST)
                if form.is_valid:
                    new_org = form.save(commit=False)
                    new_org.responsable = request.user
                    new_org.save()
                    redirect('index')
        except ValueError:
            return render(request, "registration/organizacion.html", {
                'form': OrganizacionForm,
                'error': 'please provide valude data'
            })


def voluntario(request):
    if request.method == 'GET':
        voluntarios = Voluntario.objects.filter(supervisor__isnull = True, tipo_voluntario = 'C')
        return render(request, 'voluntario.html', {
            'voluntarios': voluntarios
        })
    else:
        try:
            if request.method == 'POST':
                voluntario = Voluntario.objects.filter(tipo_voluntario = 'R')
                if voluntario.user == request.user:
                    voluntario.supervisor = request.supervisor
                    voluntario.save()
        except IntegrityError:
            return render(request, 'voluntario.html', {
                'voluntarios': voluntarios,
                'error': 'please provide valude data'
            })
        

def mensaje(request):
    if request.method == 'GET':
        return render(request, 'mensaje.html')
    else:
            try:
                    if request.method == 'POST':
                        message = request.POST['message']
                        send_mail(
                            request.POST['subject'],
                            message,
                            request.POST['email'],
                            ['coilaloki87@gmail.com'],
                            fail_silently=False,
                        )
                        return redirect('index')
            except IntegrityError:
                    return render(request, 'mensaje.html', {
                        "error": 'password do not match'
                    })

def edit(request):
    return render(request, 'registration/edit.html')

def password(request):
    return render(request, 'registration/password.html')

def emailsentconfirm(request):
    return render(request, 'registration/emailsentconfirm.html')

def about(request):
    return render(request, 'about.html')

def collect(request):
    return render(request, 'collect.html')

def contact(request):
    return render(request, 'contact.html')

def delivery(request):
    return render(request, 'delivery.html')

def donationdetails(request):
    return render(request, 'donationdetails.html')

def food(request):
    return render(request, 'food.html')

def money(request):
    return render(request, 'money.html')

def question(request):
    return render(request, 'question.html')

def services(request):
    return render(request, 'services.html')

def sampleinnerpage(request):
    return render(request, 'sampleinnerpage.html')



def donaciones(request):
    items = TransaccionItems.objects.all()
    return render(request, 'product.html',{
        'items': items
    })

@login_required
def donaciones_productos(request):
    items = TransaccionItems.objects.filter(datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'detailproduct.html',{
        'items': items,
    })

@login_required
def subir_economica(request):
    product = Producto.objects.all()
    if request.method == 'GET':
        return render(request, 'economicaform.html', {
            'form': EconomicaForm,
            'product': product
        })
    else:
        try:
            form = ProductForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('donaciones') 
        except ValueError:
            return render(request, 'economicaform.html', {
                'form': EconomicaForm,
                'error': 'please provide valude data'
            })

@login_required
def subir_bisuteria(request):
    product = Producto.objects.all()
    if request.method == 'GET':
        return render(request, 'bisuteriaform.html', {
            'form': BisuteriaForm,
            'product': product
        })
    else:
        try:
            form = ProductForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('donaciones') 
        except ValueError:
            return render(request, 'bisuteriaform.html', {
                'form': BisuteriaForm,
                'error': 'please provide valude data'
            })

@login_required
def subir_alimento(request):
    product = Producto.objects.all()
    if request.method == 'GET':
        return render(request, 'footform.html', {
            'form': AlimentoForm,
            'product': product
        })
    else:
        try:
            form = ProductForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('donaciones') 
        except ValueError:
            return render(request, 'footform.html', {
                'form': AlimentoForm,
                'error': 'please provide valude data'
            })

@login_required
def subir_producto(request):
    product = Producto.objects.all()
    if request.method == 'GET':
        return render(request, 'productform.html', {
            'form': ProductForm,
            'product': product
        })
    else:
        try:
            form = ProductForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('donaciones') 
        except ValueError:
            return render(request, 'productform.html', {
                'form': ProductForm,
                'error': 'please provide valude data'
            })


def cantidad_donaciones(request):
    if request.method == 'GET':
        items = TransaccionItems.objects.all()
        return render(request, 'donateform.html', {
            'title': 'home',
            'form': DonationForm
        })
    else:
        try:
            if request.method == 'POST':
                form = DonationForm(request.POST)
                if form.is_valid:
                    form.save()
                    if request.POST['categoria'] == 'P':
                        return redirect('subir_producto')
                    elif request.POST['categoria'] == 'A':
                        return redirect('subir_alimento')
                    elif request.POST['categoria'] == 'B':
                        return redirect('subir_bisuteria')
                    elif request.POST['categoria'] == 'E':
                        return redirect('subir_economica')
            
        except ValueError:
            return render(request, 'donateform.html', {
                'items': items,
                'title': 'home',
                'formD': DonationForm,
                'error': 'please provide valude data'
        })


@login_required
def detalle_producto(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Producto, pk=product_id)
        form = ProductForm(instance=product)
        return render(request, 'editproduct.html', {
            'product': product,
            'form': form
        })
    else:
        try:
            product = get_object_or_404(Producto, pk=product_id)
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect('products')
        except ValueError:
            return render(request, 'editproduct.html', {
            'product': product,
            'form': form,
            'error': 'Error updating product'
        })


@login_required
def entrega_producto(request, product_id):
    product = get_object_or_404(Producto, pk=product_id)
    if request.method == 'POST':
        product.fecha = timezone.now()
        product.save()
        return redirect('produtos')


@login_required
def borrar_producto(request, product_id):
    product = get_object_or_404(Producto, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')


def transaccion(request):
    return render(request, "transaccion.html", {
        'form': TransaccionForm
    })
