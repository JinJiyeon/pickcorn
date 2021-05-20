from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from django.http import JsonResponse
from django.core import serializers
from .serializers import MovieSerializers
from rest_framework.response import Response


# Create your views here.
def recommend(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    data = serializers.serialize('json', [movie])
    context = {
        'data': data
    }
    return render(request, 'movies/recommend.html', context)