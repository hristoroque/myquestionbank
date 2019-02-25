from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest,HttpResponseRedirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_auth

def loginpage(request):
    return render(request,'question_app/login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login_auth(request,user)
        return HttpResponseRedirect(reverse('question:main'))
    else :
        return HttpResponse("jajaj")

def index(request):
    return render(request,'question_app/index.html')

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('question:index'))
    
def main(request):
    return render(request,'question_app/main.html',context = {'user': request.user})