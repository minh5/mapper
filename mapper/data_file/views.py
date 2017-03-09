import os

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import DataFile
# from .forms import DataForm


class MapView(CreateView):
    model = DataFile
    template_name = 'data_file.html'
    fields = ['name', 'uploaded_file']

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['MAPBOX_KEY'] = os.environ.get('MAPBOX_KEY')
        return context


def model_form_upload(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'templates/data_file.html', {
        'form': form
    })
