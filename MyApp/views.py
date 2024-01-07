from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Services, News

def home(request):
    return render(request, "index.html")

def view_services(request):
    try:
        services = Services.objects.all()
        response_content = ""
        for service in services:
            response_content += f"Services: {services.name}, {services.details}, {services.icon}\n"
        return HttpResponse(response_content)
    except Services.DoesNotExist:
        return HttpResponse("No services found")
def view_news(request):
    try:
        news = News.objects.all()
        response_content = ""
        for new in news:
            response_content += f"News: {new.title}, {new.details}, {new.img}\n"
        return HttpResponse(response_content)
    except News.DoesNotExist:
        return HttpResponse("No news found")

def update_service(request):
    try:
        service = Services.objects.get(id=1)
        service.name = 'Updated Name'
        service.details = 'Updated Details'
        service.icon = 'updated_image.jpg'
        service.save()
        return HttpResponse("Service updated successfully")
    except Services.DoesNotExist:
        raise Http404("Service does not exist")

def update_news(request):
    try:
        new = News.objects.get(id=1)
        new.num_of_comments = 1
        new.title = 'Updated Title'
        new.details = 'Updated Details'
        new.img = 'updated_image.jpg'
        new.save()
        return HttpResponse("News updated successfully")
    except News.DoesNotExist:
        raise Http404("News does not exist")

def delete_service(request):
    try:
        service = Services.objects.get(id = 2)
        service.delete()
        return HttpResponse("Service deleted succesfully")
    except Services.DoesNotExist:
        raise Http404("Service does not exist")
    
def delete_news(request):
    try:
        new = News.objects.get(id=2)  # Replace 2 with the desired ID
        new.delete()
        return HttpResponse("News deleted successfully")
    except News.DoesNotExist:
        raise Http404("News does not exist")

def create_service(request):
    service = Services.objects.create(
        name="birinchi service",
        details="service uchun misol",
        icon="image.jpg"
    )
    return HttpResponse("Service created succesfully")

def create_news(request):
    new = News.objects.create(
        num_of_comments=1,
        title="birinchi yangilik",
        details="yangilik uchun misol",
        img="image.jpg"
    )
    return HttpResponse("News created successfully")

