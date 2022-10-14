from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        User.objects.create_user(username=username, password=password,phone=phone,address=address)
        return redirect('users:login')

def login_page(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect('users:home')
        else:
            return HttpResponse('로그인 실패')

def home(request):
    return render('home.html')
        
        