import os

from django.views.generic.detail import DetailView

from .models import MapMaker


class MapView(DetailView):
    model = MapMaker
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['MAPBOX_KEY'] = os.environ.get('MAPBOX_KEY')
        context['mapmaker'] = model
        context['target_column']
        return context
