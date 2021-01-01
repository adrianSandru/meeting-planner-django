from django.urls import path
from . import views

urlpatterns = [
    path('home', views.greetings, name="home"),
    path('login', views.loginPage, name="login"),
    path('registration', views.registrationPage, name="registration"),
    path('about', views.about, name = "about")
]