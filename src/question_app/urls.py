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