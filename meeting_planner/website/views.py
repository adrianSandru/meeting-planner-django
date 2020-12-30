from django.shortcuts import render
from django.http import HttpResponse
from datetime import  datetime

from meetings.models import Meeting
# Create your views here.
def greetings(request):
    return render(request,"website/greetings.html",
                    {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("The current date is:"+ str(datetime.now()))

def about(request):
    return HttpResponse("About Page View")