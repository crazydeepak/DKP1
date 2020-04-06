from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html',{'name':"Deepak"})

def add(request):
    n1=request.POST['num1']
    n2=request.POST['num2']
    result=int(n1)+int(n2)
    return render(request,'result.html',{'res':result})