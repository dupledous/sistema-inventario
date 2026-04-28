from django.contrib import admin
from django.urls import path
from . import views

app_name= 'account'
urlpatterns = [
    path('registrar/',views.signup,name='registrar'),
]