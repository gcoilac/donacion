from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Producto, TransaccionItems
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PersonaNaturalForm, VoluntarioForm, OrganizacionForm, ProductForm, DonationForm
#from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html', {
        'form': UserCreationForm
    })
    else:
            if request.POST['password1'] == request.POST['password2']:
                #register user
                try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('solicitud')
                except IntegrityError:
                    return render(request, 'users/signup.html', {
                        'form': UserCreationForm,
                        "error": 'User already exists'
                    })
    return render(request, 'users/signup.html', {
    'form': UserCreationForm,
    "error": 'password do not match'
    })

def signin(request):
    if request.method == 'GET':
        return render(request, 'users/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username = request.POST['username'], password = request.POST['password']
        )
        if user is None:
            return render(request, 'users/signin.html', {
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


def perfil(request):
    return render(request, 'users/solicitude.html')

def solicitud(request):
    status = request.GET['status']
    if(status == '1'):
        return redirect('solicitudVoluntario')
    elif(status == '2'):
        return redirect('solicitudPersona')
                
@login_required
def solicitudVoluntario(request):
    if request.method == 'GET':
        return render(request, 'users/voluntario.html', {
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
            return render(request, 'users/solicitude.html', {
                'form': VoluntarioForm(),           
                'error': 'please provide valude data'
            })
                
@login_required
def solicitudPersona(request):
    if request.method == 'GET':
            return render(request, 'users/persona.html', {
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
            return render(request, 'users/solicitude.html', {
                'form': PersonaNaturalForm(),           
                'error': 'please provide valude data'
            })
        
def solicitudOrganizacion(request):
    if request.method == 'GET':
        return render(request, "users/organizacion.html", {
            'form': OrganizacionForm
        })
    else:
        try:
            if request.method == 'POST':
                form = OrganizacionForm(request.POST)
                if form.is_valid:
                    new_org = form.save(commit=False)
                    new_org.responsable = request.user
                    form.save()
                    redirect('index')
        except ValueError:
            return render(request, "users/organizacion.html", {
                'form': OrganizacionForm,
                'error': 'please provide valude data'
            })


def edit(request):
    return render(request, 'users/edit.html')

def password(request):
    return render(request, 'users/password.html')

def emailsentconfirm(request):
    return render(request, 'users/emailsentconfirm.html')

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



def transaccion_items(request):
    items = TransaccionItems.objects.all()
    return render(request, 'product.html',{
        'items': items
    }) 

def products(request, item_id):
    item = TransaccionItems.objects.get(pk=item_id)
    products = item.objects.filter(datecompleted__isnull=True)
    return render(request, 'detailproduct.html', {
        'products': products
    })

@login_required
def donated_products(request):
    items = TransaccionItems.objects.filter(datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'detailproduct.html',{
        'items': items,
    }) 


def cantidad_producto(request):
    if request.method == 'GET':
        items = TransaccionItems.objects.all()
        form = DonationForm()
        return render(request, 'donation/donation.html', {
            'items': items,
            'title': 'home',
            'form': DonationForm
        })
    else:
        try:
            form = DonationForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('cantidad_producto')
        except ValueError:
            return render(request, 'donation/donation.html', {
                'products': products,
                'title': 'home',
                'form': form,
                'error': 'please provide valude data'
        })


@login_required
def subir_producto(request, item_id):
    item = TransaccionItems.objects.get(pk=item_id)
    products = item.producto_set.all()
    if request.method == 'GET':
        return render(request, 'donateproduct.html', {
            'form': ProductForm,
            'products': products
        })
    else:
        try:
            item = TransaccionItems.objects.get(pk=item_id)
            products = item.producto_set.all()
            form = ProductForm(request.POST)
            if form.is_valid:
                newform = form.save(commit=False)
                newform.transaccion_item = request.item
                form.save()
                return redirect('products') 
        except ValueError:
            return render(request, 'donateproduct.html', {
                'form': ProductForm,
                'error': 'please provide valude data'
            })


@login_required
def detalle_Producto(request, product_id):
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

