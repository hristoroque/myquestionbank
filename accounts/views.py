from django.shortcuts import render,reverse
from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request,username=name,password=password)
            print("authenticating")
            if user is not None:
                print("user autehnticated")
                login(request,user)
                return HttpResponseRedirect(reverse('question:index'))
            else:
                message = "Youre username or password is incorrect"
                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            return render(request,'accounts/login.html')
    else:
        return HttpResponseRedirect(reverse('question:index'))

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('question:index'))
    else:
        return render('question_app/index.html')
#def signup_view():
#    return render()