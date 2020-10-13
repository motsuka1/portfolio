from django.shortcuts import render
from .models import Site

# Create your views here.
def home(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    return render(request, 'websites/main.html', context)
