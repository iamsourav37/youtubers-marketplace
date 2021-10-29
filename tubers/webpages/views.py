from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
from contacttuber.models import Contact
from django.contrib import messages as d_message
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_ytubers = Youtuber.objects.order_by("-created_date").filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by("-created_date")[:6]
    data = {
        "sliders": sliders,
        "teams": teams,
        "features": featured_ytubers,
        "tubers": all_tubers,
    }
    return render(request, "webpages/home.html", data)


def about(request):
    teams = Team.objects.all()
    data = {
        "teams": teams,
    }
    return render(request, 'webpages/about_us.html', data)


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

        # TODO: Data sanitization

        contact = Contact(full_name=full_name, phone=phone, email=email, company_name=company_name, subject=subject, message=message)
        contact.save()
        d_message.success(request, "Thank you for reaching out !!!")

    return render(request, 'webpages/contact_us.html')


