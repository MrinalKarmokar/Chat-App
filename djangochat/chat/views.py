from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html')

def room(request, room_id):
    context = {
        'room_id': room_id
    }
    return render(request, 'room.html')