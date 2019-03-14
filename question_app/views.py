from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from . import models

def index(request):
    if request.user.is_authenticated:
        return render(request,'question_app/main.html',context={"user": request.user})
    else:
        return render(request,'question_app/index.html')

def themes(request):
    user = request.user
    if user.is_authenticated:
        themes = models.Theme.objects.filter(user_id = request.user)
        return render(request,'question_app/themes.html',context={'themes': themes})

def theme(request,theme_pk):
    user = request.user
    if user.is_authenticated:
        theme = models.Theme.objects.get(pk = theme_pk)
        questions = models.Question.objects.filter(themes = theme)
        return render(request,'question_app/theme.html',context={'questions': questions,'theme': theme})

def new_theme(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            theme_name = request.POST['theme_name']
            theme_description = request.POST['theme_description']
            theme = models.Theme(theme_name = theme_name,theme_description = theme_description,user_id = user)
            theme.save()
            return HttpResponseRedirect(reverse('question:themes'))
        else:
            return render(request,'question_app/theme_creation.html')

def edit_theme(request,theme_pk):
    user = request.user
    if user.is_authenticated:
        theme = models.Theme.objects.get(pk=theme_pk)
        if request.method == "POST":
            theme_name = request.POST['theme_name']
            theme_description = request.POST['theme_description']
            theme.theme_name = theme_name
            theme.theme_description = theme_description
            theme.save()
            return HttpResponseRedirect(reverse('question:themes'))
        else:
            return render(request,'question_app/theme_edit.html',context={'theme': theme})

def delete_theme(request,theme_pk):
    user = request.user
    if user.is_authenticated:
        theme = models.Theme.objects.get(pk = theme_pk)
        theme.delete()
        return HttpResponseRedirect(reverse('question:themes'))

def new_question(request,theme_pk):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            answer = request.POST['answer']
            question = models.Question(question_text = name,answer = answer,user_id = user, use_rate = 0)
            question.save()
            theme = models.Theme.objects.get(pk = theme_pk)
            theme.question_set.add(question)
            return HttpResponseRedirect(reverse('question:theme',args=[theme_pk]))
        else:
            return render(request,'question_app/question_creation.html',context={'theme_pk': theme_pk})

def edit_question(request,theme_pk,question_pk):
    user = request.user
    if user.is_authenticated:
        question = models.Question.objects.get(pk = question_pk)
        if request.method == "POST":
            text = request.POST['name']
            answer = request.POST['answer']
            question.question_text = text
            question.answer = answer
            question.save()
            return HttpResponseRedirect(reverse('question:theme',args=[theme_pk]))
        else:
            return render(request,'question_app/update_question.html',context={'theme_pk': theme_pk,'question': question})

def delete_question(request,theme_pk,question_pk):
    user = request.user
    if user.is_authenticated:
        question = models.Question.objects.get(pk = question_pk)
        question.delete()
        return HttpResponseRedirect(reverse('question:theme',args=[theme_pk]))
        

'''
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
'''