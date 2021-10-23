from django.http.request import QueryDict
from django.shortcuts import get_object_or_404, render
from .models import Youtuber


# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.order_by("-created_date")
    data = {
        "tubers": tubers,
    }
    return render(request, "youtubers/youtubers.html", data)


def youtuber_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber,
    }
    return render(request, "youtubers/youtuber_detail.html", data)



def search(request):
    tubers = set()
    data = {}

    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers_name_search = Youtuber.objects.filter(name__icontains=keyword)
            tubers_description_search = Youtuber.objects.filter(description__icontains=keyword)
            print(tubers_name_search)
            print(tubers_description_search)
            tubers = tubers.union(tubers_name_search, tubers_description_search)
            print(tubers)

            if not tubers:
                data['message'] = "No result found !!!"    
        else:
            tubers = Youtuber.objects.order_by("-created_date")


    data["tubers"] = tubers
    
    return render(request, "youtubers/search.html", data)
