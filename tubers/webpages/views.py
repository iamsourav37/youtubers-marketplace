from django.shortcuts import render
from .models import Slider, Team
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    data = {
        "sliders": sliders,
        "teams": teams,
    }
    return render(request, "webpages/home.html", data)


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    pass


def contact(request):
    pass

