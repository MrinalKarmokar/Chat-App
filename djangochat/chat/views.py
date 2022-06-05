from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Message

# Create your views here.


@login_required
def index(request):
    context = {}
    return render(request, 'chat/index.html', context)


@login_required
def home(request):
    context = {
        'first_name': request.session['first_name']
    }
    if request.method == 'POST':
        roomid = request.POST['roomid']

        return redirect(f'/chat/{roomid}')
    return render(request, 'chat/home.html', context)


@login_required
def chatroom(request, room_id):
    messages = Message.objects.filter(slug=room_id)[0:25]
    context = {
        'room_id': room_id,
        'messages': messages,
    }
    return render(request, 'chat/chatroom.html', context)
