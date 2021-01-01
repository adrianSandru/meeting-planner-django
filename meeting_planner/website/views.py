from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from datetime import  datetime

from meetings.models import Meeting
from .forms import CreateUserForm

# Create your views here.
def greetings(request):
    return render(request,"website/greetings.html",
                    {"meetings": Meeting.objects.all()})

def about(request):
    return HttpResponse("About Page View")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        
    return render(request, "website/login.html")

def registrationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect("login")

    return render(request, "website/registration.html", {'form': form})