from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Hiretuber
from django.contrib import messages
# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']
        message = request.POST['message']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        user_id = request.POST['user_id']
        state = request.POST['state']

        # TODO: do sanitization of the data

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, city=city, phone=phone, message=message, tuber_id=tuber_id, tuber_name=tuber_name, user_id=user_id, state=state)
        hiretuber.save()
        messages.success(request, "Thanks for reaching out !")
        return redirect("youtubers")
    

