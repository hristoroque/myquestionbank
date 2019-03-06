from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_auth
from django.contrib.auth.models import User

from . import models

def loginpage(request):
    return render(request,'question_app/login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login_auth(request,user)
        return HttpResponseRedirect(reverse('question:main',args=[username]))
    else :
        return HttpResponse("jajaj")

def index(request):
    return render(request,'question_app/index.html')

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('question:index'))
    
def main(request,username):
    return render(request,'question_app/main.html',context = {'user': request.user})

def questions(request):
    user = request.user
    themes = models.Theme.objects.filter(user_id = user)
    return render(request,'question_app/questions.html',context = {'themes' : themes} )

def question_creation(request,username,theme_pk):
    return render(request,'question_app/question_creation.html',context = {'theme_pk' : theme_pk})

def theme_creation(request,username):
    return render(request,'question_app/theme_creation.html')

def theme_edit(request,username,theme_pk):
    theme = models.Theme.objects.get(pk = theme_pk)
    return render(request,'question_app/theme_edit.html',context={'theme': theme})

def edit_theme(request,username,theme_pk):
    name = request.POST['theme_name']
    description = request.POST['theme_description']
    theme = models.Theme.objects.get(pk = theme_pk)
    theme.theme_name = name
    theme.theme_description = description
    theme.save()
    return HttpResponseRedirect(reverse('question:theme',args=[username,theme_pk]))

def create_theme(request,username):
    name = request.POST['theme_name']
    desc = request.POST['theme_description']
    theme = models.Theme(theme_name = name,theme_description = desc, user_id = request.user)
    theme.save()
    return HttpResponseRedirect(reverse('question:themes',args=[request.user.username]))

def delete_theme(request,username,theme_pk):
    theme = models.Theme.objects.get(pk = theme_pk)
    theme.delete()
    return HttpResponseRedirect(reverse('question:themes',args=[request.user.username]))

def create_question(request,username,theme_pk):
    name = request.POST['name']
    answer = request.POST['answer']
    themes = models.Theme.objects.get(pk=theme_pk)
    question = models.Question(question_text = name,answer = answer, user_id = request.user, use_rate=0)
    question.save()
    themes.question_set.add(question)
    
    return HttpResponseRedirect(reverse('question:theme',args=[username,theme_pk]))

def themes(request,username):
    themes = models.Theme.objects.filter(user_id = request.user)
    print(request.user)
    print(request.user.pk)
    return render(request,'question_app/themes.html',context={'themes': themes})

def theme(request,username,theme_pk):
    questions = models.Question.objects.filter(themes__pk = theme_pk)
    return render(request,'question_app/theme.html',context={'questions': questions,'theme_pk': theme_pk})

def tests(request,username):
    tests = models.Test.objects.filter(user_id = request.user)
    return render(request,'question_app/tests.html',context={'tests': tests})

def test_creation(request,username):
    themes = models.Theme.objects.filter(user_id = request.user.id)
    return render(request,'question_app/test_creation.html',context={"themes":themes})

def create_test(request,username):
    theme_pk = request.POST['theme']
    name = request.POST['name']
    theme = models.Theme.objects.get(pk = theme_pk)
    questions = models.Question.objects.filter(themes = theme).order_by('-use_rate')[:10]
    test = models.Test.objects.create(test_name=name , user_id = request.user )
    test.save()
    for question in questions:
        test.testquestion_set.create(question_id = question,score = 0)
    return HttpResponseRedirect(reverse('question:tests',args=[request.user.username]))

def test(request,username,test_pk):
    test = models.Test.objects.get(pk = test_pk)
    return render(request,'question_app/test.html',context = {'test': test})

def test_taking(request,username,test_pk):
    test = models.Test.objects.get(pk = test_pk)
    return render(request,'question_app/test_taking.html',context={'test': test})

def take_test(request,username,test_pk):
    test = models.Test.objects.get(pk = test_pk)
    graded_test = models.GradedTest(test_id = test,user_id = request.user, grade = 0)
    graded_test.save()
    for testquestion in test.testquestion_set.all():
        question = testquestion.question_id
        string = 'answer-%d' %question.pk 
        print(string)
        answer = request.POST[string]
        graded_test.gradedtestquestion_set.create(
            question_name = question.question_text,
            user_answer = answer,
            grade = 0
        )
    return HttpResponseRedirect(reverse('question:tests',args=[request.user.username]))

def delete_test(request,username,test_pk):
    test = models.Test.objects.get(pk = test_pk)
    test.delete()
    return HttpResponseRedirect(reverse('question:tests',args=[username]))

def tests_review(request,username):
    graded_tests = models.GradedTest.objects.filter(test_id__user_id = request.user)
    return render(request,'question_app/tests_review.html',context = { 'graded_tests': graded_tests })
    
def test_review(request,username,graded_test_pk):
    graded_test = models.GradedTest.objects.get(pk = graded_test_pk)
    test = models.Test.objects.get(pk = graded_test.test_id.pk)
    graded_questions = models.GradedTestquestion.objects.filter(test_id__pk = graded_test_pk,test_id__test_id = test)
    print(graded_questions)
    return render(request,'question_app/test_review.html',context = {'test': test,'graded_questions': graded_questions})

def test_performance(request,username):
    return render(request,'question_app/test_review.html')