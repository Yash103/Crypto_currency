from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Reg
from .forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
import requests


def registration(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           print("valid Details")
           messages.success(request, "Account created successfully!")
           return redirect('login')
        

    else:
            form = RegistrationForm()
            print("Invalid Details")

    return render(request,'registration.html', {'form':form})


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            un = request.POST.get('username')
            pwd = request.POST.get('password')
            dbuser=Reg.objects.filter(username=un,password=pwd)
            if not dbuser:
                return HttpResponse("Login Failed")
            else:
                return redirect(index)
        else:
            form = LoginForm(request.POST)
            return render(request, 'login.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        return render(request,'login.html', {'form':form})




def index(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request, 'index.html', data)


# return the data received from api as json object
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()

    return data

