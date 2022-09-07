from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Tour

# Create your views here.

def tours_list(request):
    tours = Tour.objects.all().order_by('name')
    return render(request, 'tours/tours_list.html', {'tours': tours})

def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'tours/tour_detail.html', {'tour': tour})

def test_view(request):
    html = "<html><body><h1>TEST</h1></body></html>"
    return HttpResponse(html)