from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if User.objects.filter(name=username, password=password).exists():
                return JsonResponse({'success': True})
            else:
                if User.objects.filter(name=username).exists():
                    return JsonResponse({'success': False, 'message': 'Wrong password'})
                else:
                    return JsonResponse({'success': False, 'message': 'User does not exist'})

    return render(request, 'login.html', {'form': LoginForm()})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(name=username).exists():
            return JsonResponse({'success': False, 'message': 'User already exists'})
        else:
            user = User(name=username, password=password)
            user.save()
            return JsonResponse({'success': True})
    return render(request, 'signup.html', {'form': LoginForm()})


def users(request):
    items = User.objects.all()
    return render(request, 'users.html', {'users': items})
