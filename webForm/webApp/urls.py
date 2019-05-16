from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('webform/', views.webform, name='webform'),
    path('webform_submit/', views.webform_submit, name='webform_submit')
]
