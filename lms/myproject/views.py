from django.shortcuts import render
from django.http import HttpResponse
from myproject.models import info

# Create your views here.
def index(request):
    return render(request,'index.html');
def faq(request):
    return render(request,'faq.html');
def books(request):
    return render(request,'books.html');
def support(request):
    return render(request,'support.html');
def mybooks(request):
    return render(request,'mybooks.html');
def update(request):
    return render(request,'update.html');
def login(request):
    return render(request,'s_login.html');
def register(request):
    return render(request,'s_register.html');
def request(request):
    return render(request,'req.html');
def recover(request):
    return render(request,'recover.html');
def account_created(request):
    saverecord = info()
    saverecord.name = request.POST["name"]
    saverecord.m_no = request.POST["m_no"]
    saverecord.email = request.POST["email"]
    saverecord.password = request.POST["password"]
    saverecord.save()
    return render(request,'account_created.html');
