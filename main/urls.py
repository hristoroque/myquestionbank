from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
        path('home/',TemplateView.as_view(template_name='main/home.html'),name='home'),
        ]
