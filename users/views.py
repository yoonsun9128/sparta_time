from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
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

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        return HttpResponse('로그인 성공')
        