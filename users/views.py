from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "users/index.html")
    

def login_view(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            contex = {
                "message": "incorrect credentials"
            }
            return render(request, "users/login.html", contex)

    return render(request, "users/login.html") 



def logout_view(request):
    logout(request)
    contex={
        "message": "Logged Out"
    }
    return render(request, "users/login.html", contex)
