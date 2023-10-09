from django.shortcuts import render
from .models import Movie
from django.http import Http404
from movies.forms import MovieForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect

def index(request):
    newest_movies = Movie.objects.order_by('-year')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})
  
def new(request):
  return render(request, 'movies/New.html')
  
def newRecord(request):
  if request.method == 'POST':
    form = MovieForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
    return render(request, 'movies/index.html', {'newest_movies': Movie.objects.order_by('-year')[:15]})

def update(request, id):
  movie = Movie.objects.get(id=id)
  template = loader.get_template('movies/update.html')
  context = {
    'movie': movie,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecord(request, id):
  movie = Movie.objects.get(pk=id)
  form = MovieForm(request.POST,request.FILES, instance = movie)
  if form.is_valid():
     form.save()
     return redirect('/movies/{}'.format(id))
    # return HttpResponseRedirect(reverse('movies/show'))
    # return render(request, 'movies/show.html', {'movie': movie})
  else:
    return render(request, 'movies/index.html', {'movie': movie})
  
def delete(request, id):
  movie = Movie.objects.get(id=id)
  movie.delete()
  return render(request, 'movies/index.html', {'newest_movies': Movie.objects.order_by('-year')[:15]})
