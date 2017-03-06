import os

from django.shortcuts import render
from django.views.generic import ListView

from .models import DataFile

# Create your views here.
class MapView(ListView):
    model = DataFile
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        print('Hello World')
        context = super(MapView, self).get_context_data(**kwargs)
        context['MAPBOX_KEY'] = os.environ.get('MAPBOX_KEY')
        context['Hi'] = 'test'
        return context
