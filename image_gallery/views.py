from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

# Create your views here.
def index(request):
    image = Image.objects.all()
    
    context= {
        'image': image
    }

    return render(request, 'gallery/index.html', context)

def search_results(request):

    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        context = {
            "message": message, 
            "images": searched_images
        }
        print(searched_images)
        return render(request, 'gallery/search_res.html', context)
    else:
        message = "You haven't searched for any image category"

        return render(request, 'gallery/search_res.html', {"message": message})
