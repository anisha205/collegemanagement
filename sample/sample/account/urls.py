from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.mainhome,name='mainhome'),
    path('contact/',views.contact,name='contact'),
    path('course/',views.course,name='course'),
    path('gallery/',views.gallery,name='gallery'),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name='signup'),
    path('password/',views.password,name='password'),
    path('loginhome/',views.loginhome,name='loginhome'),

]