from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacttuber.models import SocialLink
# Create your views here.


def register(request):
    data = {
        "social_links": SocialLink.objects.first(),
    }
    if request.method == 'POST':
        firstname = request.POST['firstname'].strip()
        lastname = request.POST['lastname'].strip()
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(f"firstname: {firstname}")

        if not (firstname and lastname and username and email and password1):
            messages.error(request, "**All the fields are required.")
            return redirect("register")
        if len(password1) < 4:
            messages.error(request, "**Password must be 4 character long.")
            return redirect("register")
        if password1 == password2:
            print("password is matched")

            if User.objects.filter(username=username).exists():
                messages.error(request, f"** '{username}' is already exists.")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, f"** '{email}' is already exists.")
                return redirect("register")
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password1)
                user.save()
                print("account is saved in db")
                messages.success(request, "Account created successfully")
                return redirect("login")

        else:
            messages.error(request, "** Password is not matched")
            return redirect("register")

        

    return render(request, "accounts/register.html", data)


def login(request):
    data = {
        "social_links": SocialLink.objects.first(),
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in !!!")
            return redirect("dashboard")
        else:
            messages.error(request, "** Invalid credentials")
            return redirect("login")
    return render(request, "accounts/login.html", data)


def logout_user(request):
    logout(request)
    return redirect("webpages.home")

@login_required(login_url="login")
def dashboard(request):
    data = {
        "social_links": SocialLink.objects.first(),
    }
    return render(request, "accounts/dashboard.html", data)
