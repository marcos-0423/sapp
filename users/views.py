from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
     return HttpResponseRedirect(reverse("login"))
def login_view(request):
    # Handle login logic here
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {"error": "Invalid username or password."})
            
    # ⚠️ أضف هذا السطر هنا وتأكد من محاذاته مع سطر الـ if بالرقم 14:
    return render(request, "users/login.html")



       


def logout_view(request):
  pass