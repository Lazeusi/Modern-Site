from django.shortcuts import render
from .models import SlideImges
# Create your views here.

def home(request):
    images = SlideImges.objects.all()
    return render(request, 'pages/index.html' , {'images':images})