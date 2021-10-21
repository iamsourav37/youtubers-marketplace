from django.shortcuts import render
from .models import Slider
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    data = {
        "sliders": sliders
    }
    return render(request, "webpages/home.html", data)


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    pass


def contact(request):
    pass

