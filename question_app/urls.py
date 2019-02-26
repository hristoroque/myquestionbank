from django.urls import path
from . import views
# Create your views here.

app_name = "question"
urlpatterns = [
    path('log/',views.loginpage,name='loginpage'),
    path('login/',views.login,name="login"),
    path('main/',views.main,name='main'),
    path('logout/',views.log_out,name='logout'),
    path('',views.index,name="index"),
    path('main/questions',views.questions,name="questions"),
    path('main/questions/creation/<int:theme_id>/',views.questioncreation,name="questioncreation"),
    path('main/questions/theme_creation/',views.themecreation,name="themecreation"),
    path('main/questions/theme_creation/create/',views.createtheme,name ="createtheme"),
    path('main/questions/creation/<int:theme_id>/create/',views.createquestion,name='createquestion')
]   