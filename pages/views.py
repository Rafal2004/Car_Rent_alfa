from email.quoprimime import body_length

from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.shortcuts import render
from .models import Car,  Car_Model, Car_Brand, Gearbox
from .forms import AddCarForm
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def home(request):
    cars = Car.objects.order_by('-created_date')[:3]
    data = {
        "cars": cars,
    }
    return render(request, 'pages/home.html', data)


def add_car(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddCarForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user

                form.save()
                return redirect("home")
            else:
                print(f" error - {form.errors} - error")

        else:
            form = AddCarForm()

        return render(request, 'pages/add_car.html', {'form': form})
    else:
        return redirect('login_user')


def rent_car(request):
    
    
    cars = Car.objects.order_by('-created_date')
    brands=Car_Brand.objects.all()
    brands_id_search = Car.objects.values_list('brand', flat=True).distinct()
    avaible_brands =[]
    for brand_id_search in brands_id_search:
        print(avaible_brands)
        avaible_brands.append(brands.filter(pk=brand_id_search))
    body_type = Car.objects.values_list(
        'body_type', flat=True).distinct()
    
    gearbox = Car.objects.values_list('gearbox', flat=True).distinct()    

    if 'brand' in request.GET:
            brand= request.GET['brand']
            if brand != 'All':
              cars = cars.filter(brand=brand)
       
    if 'gearbox' in request.GET:
        gearbox = request.GET['gearbox']
        if gearbox!='All':
            cars = cars.filter(gearbox=gearbox)

    data = {
        "cars": cars,
        'gearbox': gearbox,             
        'brand_search':avaible_brands,
        'body_type' : body_type

    }

    return render(request, 'pages/rent_car.html', data)


def detail_car(request, pk):
    car = Car.objects.filter(pk=pk).first()
    data = {
        'car': car,
    }
    return render(request, 'pages/details_car.html', data)


def my_account(request, views):
    cars = Car.objects.filter(user=request.user)
    data = {
        'cars': cars,
        'views': views,
    }
    
    return render(request, 'pages/my_account.html', data)


def edit_car(request,pk):
  
    if request.user.is_authenticated:
            old_form = Car.objects.filter(pk=pk).first()
            if request.method == 'POST':
                
                form = AddCarForm(request.POST, request.FILES, instance=old_form)
                if form.is_valid():
                    form.instance.user = request.user

                    form.save()
                    return redirect("home")
                else:
                    print(f" error - {form.errors} - error")

            else:
                form = AddCarForm(instance=old_form)

            return render(request, 'pages/edit_car.html', {'form': form})
    else:
        return redirect('login_user')
