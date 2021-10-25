from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
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
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact_us.html')


