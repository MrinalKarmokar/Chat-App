from django import urls
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'chat/index.html', context)

def home(request):
    context = {
        'first_name': request.session['first_name']
    }
    if request.method == 'POST':
        roomid = request.POST['roomid']
        return redirect(f'/chat/{roomid}')
    return render(request, 'chat/home.html', context)

def room(request, room_id):
    context = {
        'room_id': room_id,
    }
    return render(request, 'chat/room.html', context)