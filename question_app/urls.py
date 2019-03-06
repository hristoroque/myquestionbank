from django.urls import path
from . import views
# Create your views here.

app_name = "question"
urlpatterns = [
    path('log/',views.loginpage,name='loginpage'),
    path('login/',views.login,name="login"),
    path('<str:username>/',views.main,name='main'),
    path('logout/',views.log_out,name='logout'),
    path('',views.index,name="index"),
    path('<str:username>/themes/',views.themes,name="themes"),
    path('<str:username>/themes/<int:theme_pk>',views.theme,name="theme"),
    path('<str:username>/themes/creation',views.theme_creation,name="theme_creation"),
    path('<str:username>/themes/<int:theme_pk>/creation',views.question_creation,name="question_creation"),
    path('<str:username>/themes/<int:theme_pk>/delete',views.delete_theme,name="delete_theme"),
    path('<str:username>/themes/<int:theme_pk>/edit',views.theme_edit,name='theme_edit'),
    path('<str:username>/themes/<int:theme_pk>/editing',views.edit_theme,name='edit_theme'),
    path('<str:username>/tests/',views.tests,name="tests"),
    path('<str:username>/tests/creation',views.test_creation,name="test_creation"),
    path('<str:username>/tests/create',views.create_test,name="create_test"),
    path('<str:username>/themes/create',views.create_theme,name ="create_theme"),
    path('<str:username>/themes/<int:theme_pk>/create',views.create_question,name='create_question'),
    path('<str:username>/tests/<int:test_pk>',views.test,name="test"),
    path('<str:username>/tests/<int:test_pk>/exam',views.test_taking,name="test_taking"),
    path('<str:username>/tests/<int:test_pk>/take',views.take_test,name="take_test"),
    path('<str:username>/tests/review',views.tests_review,name="tests_review"),
    path('<str:username>/tests/review/<int:graded_test_pk>',views.test_review,name="test_review"),
    path('<str:username>/tests/review',views.test_performance,name='test_performance'),
    path('<str:username>/tests/<int:test_pk>/delete',views.delete_test,name='delete_test')
]   