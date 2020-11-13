from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie

# Create your views here.
class MovieList(ListView):
    model = Movie
