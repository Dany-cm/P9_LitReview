from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def view_index(request):
    return render(request, 'base.html')


def view_register(request):
    if request.user.is_authenticated:
        return redirect('base.html')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('test.html')
        else:
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'register.html', context)
    return render(request, 'base.html')


def view_login(request):
    if request.user.is_authenticated:
        return redirect('base.html')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('base.html')
        else:
            form = AuthenticationForm()
            context = {'form': form}
            return render(request, 'login.html', context)
    return render(request, 'base.html')


def view_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('base.html')
