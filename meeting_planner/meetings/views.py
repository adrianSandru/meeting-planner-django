from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room

# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def list_rooms(request):
    room = Room.objects.all()
    return render(request, "meetings/rooms.html", {"rooms": room})

def new_meeting(request):
    return render(request, 'meetings/new.html')