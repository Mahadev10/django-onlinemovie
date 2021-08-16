from django.shortcuts import render
from .models import Movie
# Create your views here.
def home(request):
    movie_data=Movie.objects.filter(show=True)
    print(movie_data)
    return render(request,"home.html",context={"movies":movie_data})

def testimonials(request):
    return render(request,"testimonials.html",{})