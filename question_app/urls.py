from django.urls import path
from . import views
# Create your views here.

app_name = "question"
urlpatterns = [
    path('log/',views.loginpage,name='loginpage'),
    path('login/',views.login,name="login"),
    path('main/',views.main,name='main'),
    path('logout/',views.log_out,name='logout'),
    path('',views.index,name="index")
]   