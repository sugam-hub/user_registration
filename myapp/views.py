from cgitb import text
import email
from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.GET['text']
    amount_of_word = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_word})


def register(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['password2']

        if password == repeat_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect("register")

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exist")
                return redirect("register")

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                messages.info(request, "User Created Successfully")
                return redirect("register")
        else:
            messages.info(request, "Password doesn't match")
            return redirect("register")

    else:
        return render(request, "register.html")


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")

        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")

    else:
        return render(request, 'login.html')


def home(request):
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})


def counter1(request):
    posts = [1, 2, 3, 4, 5, 'sugam', 'anish', 'kaka']
    return render(request, 'counter1.html', {'posts': posts})
