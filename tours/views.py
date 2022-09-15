from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest

from .models import Tour, Stop, Block, Keyword

# Create your views here.

def tours_list(request):
    tours = Tour.objects.all().order_by('name')
    return render(request, 'tours/tours_list.html', {'tours': tours})

def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    stops = Stop.objects.filter(tour=tour.pk)
    blocks = Block.objects.filter(stop__in=stops)
    block_keyword_list = []
    for block in blocks:
        for kw in block.keywords.all():
            block_keyword_list.append(kw)
    return render(request, 'tours/tour_detail.html', {'tour': tour, 'keywords': block_keyword_list,})

def test_view(request):
    html = "<html><body><h1>TEST</h1></body></html>"
    return HttpResponse(html)

def tour_generated(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    picked_keywords = []
    print(request.GET.dict().keys())
    for name, value in request.GET.items():
        if name.startswith('kw-'):
            picked_keywords.append(int(value))
    stops = Stop.objects.filter(tour=tour.pk)
    unskippable_blocks = Block.objects.filter(stop__in=stops, skippable=False).distinct()
    picked_blocks = Block.objects.filter(stop__in=stops, keywords__id__in=picked_keywords).distinct()
    blocks = unskippable_blocks | picked_blocks
    blocks = blocks.order_by('stop__order', 'order')

    # TODO: Pass the blocks not as one list, but grouped by stop
    #  so that we can, in the template, write individual stop information as well
    return render(request, 'tours/tour_generated.html', {'tour': tour, 'blocks': blocks,})