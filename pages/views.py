from django.shortcuts import render, get_object_or_404
from .models import Announcement

# Create your views here.

def home(request):
    context = {
        'title': 'Home', 
        'features': [
            'Django', 
            'Templates', 
            'Static Files'
        ]
    }
    return render(request, 'home.html', context)

def announcement_list(request):
    announcements = Announcement.objects.all().order_by("-created_at")
    return render(request, "announcements/list.html", {"announcements": announcements})

def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, "announcements/detail.html", {"announcement": announcement})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)