from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

import requests
import json

def home(request):


    # Crypto Price

    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,NMC,PPC,GRC,LTC,NXT,AUR,DASH,XMR,XEM,POT,ETC,ZEC,EOS&tsyms=USD")

    price=json.loads(price_request.content)


    #Crypto News


    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")

    api=json.loads(api_request.content)

    return render(request,'home.html',{'api':api,'price':price})


def prices(requests):

    if requests=='POST':
        quote=requests.POST['quote']
        quote.upper()
        crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD")
        crypto=json.loads(crypto_request.content)

        return render(requests,'price.html',{'quote':quote,'crypto':crypto})
    else:
        return render(requests,'price.html',{})



def aboutus(requests):

    return render(requests,'aboutus.html',{})

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

def signup(requests):
    return render(requests,'signup.html',{})
