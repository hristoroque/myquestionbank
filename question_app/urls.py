from django.urls import path
from . import views
# Create your views here.

app_name = "question"
urlpatterns = [
    path('',views.index,name='index'),
    path('themes/',views.themes,name="themes"),
    path('themes/<int:theme_pk>',views.theme,name="theme"),
    path('themes/new',views.new_theme,name="new_theme"),
    path('themes/<int:theme_pk>/edit',views.edit_theme,name="edit_theme"),
    path('themes/<int:theme_pk>/delete',views.delete_theme,name="delete_theme"),
    path('themes/<int:theme_pk>/new',views.new_question,name="new_question"),
    path('themes/<int:theme_pk>/<int:question_pk>/edit',views.edit_question,name='edit_question'),
    path('themes/<int:theme_pk>/<int:question_pk>/delete',views.delete_question,name='delete_question'),
]   
'''
path('<str:username>/tests/',views.tests,name="tests"),
    path('<str:username>/tests/creation',views.test_creation,name="test_creation"),
    path('<str:username>/tests/create',views.create_test,name="create_test"),
    path('<str:username>/tests/<int:test_pk>',views.test,name="test"),
    path('<str:username>/tests/<int:test_pk>/exam',views.test_taking,name="test_taking"),
    path('<str:username>/tests/<int:test_pk>/take',views.take_test,name="take_test"),
    path('<str:username>/tests/review',views.tests_review,name="tests_review"),
    path('<str:username>/tests/review/<int:graded_test_pk>',views.test_review,name="test_review"),
    path('<str:username>/tests/review',views.test_performance,name='test_performance'),
    path('<str:username>/tests/<int:test_pk>/delete',views.delete_test,name='delete_test')
    '''