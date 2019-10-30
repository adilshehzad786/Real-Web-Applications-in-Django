from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from . import views


def login(requests):

    if requests=='post':
        username = requests.POST['username']
        password = requests.POST['password']
        user = authenticate (requests , username=username , password=password)
        if user is not None:
            login (requests , user)
            return redirect('home')

        else:
            return redirect('login')
    else:

     return render(requests,'login.html',{})

