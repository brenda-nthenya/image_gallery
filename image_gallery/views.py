from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    image = Image.objects.all()
    
    categories = Category.objects.all()


    context= {
        "image": image,
        "categories": categories
    }

    return render(request, 'gallery/index.html', context)

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"
        context = {
            "message": message, 
            "images": searched_image

        }
        return render(request, 'gallery/search_res.html', context)
    else:
        message = "You haven't searched for any image category"
        return render(request, 'gallery/search_res.html', {"message": message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-photo/image.html", {"image":image})
