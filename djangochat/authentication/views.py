from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup_view(request):

    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
            except Exception as e:
                print(e)
                messages.warning(request, "Account with this Phone No. already exists")
                return redirect('signup')

            messages.success(request, "Signup Successful")
            request.session['username'] = str(user.username)
            request.session['first_name'] = str(user.first_name)
            request.session['last_name'] = str(user.last_name)
            request.session['email'] = str(user.email)
            return redirect('home')
        
        else:
            messages.warning(request, "Password does'nt match!")
            return redirect('signup')

        
    context = {}
    return render(request, 'authentication/signup.html')

def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = str(user.username)
            request.session['first_name'] = str(user.first_name)
            request.session['last_name'] = str(user.last_name)
            request.session['email'] = str(user.email)
            context = {}
            return redirect('home')
        
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('login')

    return render(request, 'authentication/login.html')

def logout_view(request):
    '''Logging Out Users and clearing sessions'''

    logout(request)
    return redirect('index')