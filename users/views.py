from django.shortcuts import render
from .models import User
from django.http import HttpResponse
# Create your views here.

def signup(request):
    return HttpResponse('회원가입 페이지')