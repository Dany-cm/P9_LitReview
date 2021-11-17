from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import CreateUser


# Create your views here.
def view_index(request):
    return render(request, 'base.html')


def view_register(request):
    if request.user.is_authenticated:
        return redirect('flux:home')
    else:
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('accounts:index')
        else:
            form = CreateUser()
    return render(request, 'register.html', {'form': form})


def view_login(request):
    if request.user.is_authenticated:
        return redirect('flux:home')
    else:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('flux:home')
    return render(request, 'base.html')


def view_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('accounts:index')
