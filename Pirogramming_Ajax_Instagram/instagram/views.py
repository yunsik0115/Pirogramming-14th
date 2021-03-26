from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo

class PhotoLV(ListView):
    model = Photo

class PhotoDV(DetailView):
    model = Photo
# Create your views here.
