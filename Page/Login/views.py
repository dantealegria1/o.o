from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        new_user = User(name=name, password=password)
        # Check if the user exists
        if User.objects.filter(name=name, password=password).exists():
            return JsonResponse({'success': True})
        else:
            if User.objects.filter(name=name).exists():
                return JsonResponse({'success': False, 'message': 'Wrong password'})
            else:
                return JsonResponse({'success': False, 'message': 'User does not exist'})

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        new_user = User(name=name, password=password)
        try:
            new_user.save()
            return JsonResponse({'success': True})
        except:
            return JsonResponse({'success': False, 'message': 'User already exists'})
 
    return render(request, 'signup.html')

def users(request):
    items = User.objects.all()
    return render(request, 'users.html', {'users': items })