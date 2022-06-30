from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm, ChangingForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
             messages.success(request, ('Invalid data, try again'))
             return redirect('login_user')
    else:
        return render(request, 'registration/login.html')



def logout_user(request):
    logout(request)
    return redirect("home")


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

def edit_account(request):
    if request.method == 'POST':
        form = ChangingForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChangingForm(instance=request.user)
    data = {
        'form': form,
        'views' : "my_settings"
        }
    return render(request,'pages/my_account.html', data)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    data = {
        'form': form,
        'views' : "change_password"
        }
    return render(request,'pages/my_account.html', data)