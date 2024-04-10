from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Producto, Proporciona, Donacion
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, DonationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

def edit(request):
    return render(request, 'users/edit.html')

def password(request):
    return render(request, 'users/password.html')

def emailsentconfirm(request):
    return render(request, 'users/emailsentconfirm.html')


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
                    return redirect('index')         
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
            return redirect('index')
        
@login_required
def signout(request):
    logout(request)
    return redirect('index')

def productos(request):
    products = Producto.objects.all()
    return render(request, 'product.html', {
        'products': products
    })

@login_required
def productos_donados(request):
    ingresos = Proporciona.objects.filter(fecha__isnull=False).order_by('-fecha')
    return render(request, 'product.html',{
        'ingresos': ingresos
    })

@login_required
def Donar_producto(request):
    if request.method == 'GET':
        return render(request, 'donateproduct.html', {
            'form': ProductForm
        })  
    else:
        try:
            form = ProductForm(request.POST)
            if form.is_valid:
                #newform = form.save(commit=False)
                form.save()
                return redirect('productos')
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
        return render(request, 'detailproduct.html', {
            'product': product,
            'form': form
        })
    else:
        try:
            product = get_object_or_404(Producto, pk=product_id)
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect('product'   )
        except ValueError:
            return render(request, 'detailproduct.html', {
            'product': product,
            'form': form,
            'error': 'Error updating task'
        })

@login_required
def entrega_producto(request, product_id):
    product = get_object_or_404(Proporciona, pk=product_id)
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
    
def donacion(request):
    if request.method == 'GET':
        donations = Donacion.objects.all()
        form = DonationForm()
        return render(request, 'donation/donation.html', {
            'donations': donations,
            'title': 'home',
            'form': DonationForm
        })
    else:
        try:
            form = DonationForm(request.POST)
            # if form.is_valid:
            #     form.save()
        except ValueError:
            return render(request, 'donation/donation.html', {
                'donations': donations,
                'title': 'home',
                'form': form,
                'error': 'please provide valude data'
        })