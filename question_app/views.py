from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_auth
from . import models

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

def questions(request):
    user = request.user
    themes = models.Theme.objects.filter(user_id = user.pk)
    questions 
    return render(request,'question_app/questions.html',context = {'themes' : themes} )

def questioncreation(request,theme_id):
    return render(request,'question_app/question_creation.html',context = {'theme_id' : theme_id})

def themecreation(request):
    return render(request,'question_app/theme_creation.html')

def createtheme(request):
    name = request.POST['theme_name']
    desc = request.POST['theme_description']
    theme = models.Theme(theme_name = name,theme_description = desc, user_id = request.user)
    theme.save()
    return HttpResponseRedirect(reverse('question:questions'))

def createquestion(request,theme_id):
    name = request.POST['name']
    answer = request.POST['answer']
    themes = models.Theme.objects.get(pk=theme_id)
    question = models.Question(question_text = name,answer = answer, user_id = request.user, use_rate=0)
    question.save()
    themes.question_set.add(question)
    
    return HttpResponseRedirect(reverse('question:questions'))