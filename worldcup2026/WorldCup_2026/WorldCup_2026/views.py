from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    return render(request, 'guest/index.html')

@login_required(login_url=reverse_lazy('no_access'))
def home(request):
    user = request.user
    context = {'user': user} 
    return render(request, 'logged/home.html', context)

def canada(request):
    return render(request, 'guest/cities/cn.html')

def us(request):
    return render(request, 'guest/cities/us.html')

def mexico(request):
    return render(request, 'guest/cities/mx.html')

def no_access_view(request):
    return render(request, 'no_access.html')