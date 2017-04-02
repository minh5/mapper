import os

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Column, DataFile
from .forms import DataForm, ColumnForm


class DataCreateView(CreateView):
    model = DataFile
    template_name = 'data_file.html'
    fields = ['name', 'uploaded_file']


def model_form_upload(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('column_list.html')
    else:
        form = DataForm()
    return render(request, 'data_file.html', {
        'form': form
    })


class DataDetailView(ListView):
    model = Column
    template_name = 'data_detail.html'
    fields = ['min_color', 'max_color', 'intervals']


def column_edit_form(request, id):
    instance = get_object_or_404(Column, id=id)
    form = ColumnForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
    return direct_to_template(request, 'data_detail.html', {'form': form})
