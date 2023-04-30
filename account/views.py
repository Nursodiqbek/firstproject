from django.shortcuts import render, redirect
from .models import CustomUser
from django .http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate


def register(request):

    if request.method=='POST':

        phone = request.POST.get('number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = CustomUser.objects.create(
                phone=phone,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password=password1)
    )
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('<h1>Parollarni bir xilligini qayta tekshiring!</h1>')

    return render(
        request=request,
        template_name='register.html'
    )
def log_in(request):
    if request.method == 'POST':
        phone = request.POST.get('number')
        password = request.POST.get('password')
        user = authenticate(
            phone=phone,
            password=password
        )
        if user:
            login(request,user)
            return redirect('index')
        else:
            return redirect('register')
    return render(request=request,template_name='login.html')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')


