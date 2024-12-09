from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('home')
        elif username == '':
            return render(request, 'user_management/login.html', {'message': "Ups...Parece que olvidaste escribir tu usuario."})
        elif password == '':
            return render(request, 'user_management/login.html', {'message': "Ups...Parece que olvidaste escribir tu contraseña."})
        else:
            return render(request, 'user_management/login.html', {'message': "Las credenciales son incorrectas."})
    return render(request, 'user_management/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'user_management/register.html', {'message': f"El nombre de usuario {username} ya está registrado."})
        
        elif CustomUser.objects.filter(email=email).exists():
            return render(request, 'user_management/register.html', {'message': f"El correo electrónico {email} ya está registrado."})
        
        elif password != password2:
            return render(request, 'user_management/register.html', {'message': "Revisa Las contraseñas, pues no coinciden."})
        
        else:
            user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name = last_name, email = email, photo=photo, password=password)
            user.save()
            return redirect('login')
            
    return render(request, 'user_management/register.html')

@login_required
def my_profile(request):
    user = request.user
    context = {'user': user} 
    return render(request, 'logged/my_profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')