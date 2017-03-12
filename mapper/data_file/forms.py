from django import forms

from .models import Column, DataFile

class DataForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ('name', 'uploaded_file')


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ('min_color', 'max_color', 'intervals')
