from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,Http404

from .models import Movies
def index(request):

    movies=Movies.objects.all()

    return render(request , 'movies/index.html' , {'movies':movies})

def detail(request,movie_id):
    try:
     movie=Movies.objects.get(pk=movie_id)

     return render(request,'movies/detail.html',{'movie':movie_id})

    except Movies.DoesNotExist:

        raise Http404









def empty_view(request):
    return HttpResponse ("Empty View")
