from django.http.request import QueryDict
from django.shortcuts import get_object_or_404, render
from .models import Youtuber
from contacttuber.models import SocialLink


# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.order_by("-created_date")
    data = {
        "tubers": tubers,
        "social_links": SocialLink.objects.first(),
    }

    city_list = Youtuber.objects.values_list("city", flat=True).distinct()
    camera_type_list = Youtuber.objects.values_list("camera_type", flat=True).distinct()
    category_list = Youtuber.objects.values_list("category", flat=True).distinct()
    data["city_list"] = city_list
    data["camera_type"] = camera_type_list
    data["category"] = category_list

    
    return render(request, "youtubers/youtubers.html", data)


def youtuber_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber,
        "social_links": SocialLink.objects.first(),
    }
    return render(request, "youtubers/youtuber_detail.html", data)



def search(request):
    tubers = set()
    data = {
        "social_links": SocialLink.objects.first(),
    }
    city_list = Youtuber.objects.values_list("city", flat=True).distinct()
    camera_type_list = Youtuber.objects.values_list("camera_type", flat=True).distinct()
    category_list = Youtuber.objects.values_list("category", flat=True).distinct()
    data["city_list"] = city_list
    data["camera_type"] = camera_type_list
    data["category"] = category_list

    print(f"get : {request.GET}")
    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers_name_search = Youtuber.objects.filter(name__icontains=keyword)
            tubers_description_search = Youtuber.objects.filter(description__icontains=keyword)
            tubers = tubers.union(tubers_name_search, tubers_description_search)
        
    if "city" in request.GET:
        city = request.GET['city']

        if city:
            tubers = Youtuber.objects.filter(city__iexact=city)

    if "category" in request.GET:
        category = request.GET['category']
        print("categoy: :", category)
        if category:
            tubers = Youtuber.objects.filter(category__iexact=category)
    
    if "camera" in request.GET:
        camera = request.GET['camera']
        if camera:
            tubers = Youtuber.objects.filter(camera_type__iexact=camera)


    data["tubers"] = tubers
    
    return render(request, "youtubers/search.html", data)
