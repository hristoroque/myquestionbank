from django.shortcuts import render,reverse,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from . import forms

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request,username=name,password=password)
            if user is not None:
                login(request,user)
                if 'path' in request.POST:
                    return redirect(request.POST['path'])
                else:
                    return redirect(reverse('question:main'))
            else:
                messages.warning(request,"Your username or password is incorrect")
                return redirect(reverse('accounts:login'))
        else:
            return render(request,'accounts/login.html')
    else:
        return redirect(reverse('question:main'))

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

class SignUpView(FormView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('question:main')
    template_name = 'accounts/signup.html'

    def form_valid(self,form):
        response = super().form_valid(form)
        form.save()

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')

        user = authenticate(self.request,username = username, password = raw_password)

        login(self.request,user)
        
        messages.success(self.request, "You've signed up successfully")
        return response