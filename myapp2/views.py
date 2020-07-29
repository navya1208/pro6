from django.shortcuts import render

# Create your views here.

def base(request):
  return render(request,"myapp2/base.html")

def home(request):
  return render(request,"myapp2/home.html",{"name":"Navya"})

def index(request):
  return render(request,"myapp2/index.html")

def child(request):
  return render(request,"child.html")