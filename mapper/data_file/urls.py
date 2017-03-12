from django.conf.urls import include, url
from django.contrib import admin

from .models import DataFile
from .views import DataView, ColumnView

urlpatterns = [
    url(r'^$', DataView.as_view(model=DataFile, success_url="columns"), name='data_file_create'),
    url(r'^columns/', ColumnView.as_view(), name='column_list')
    ]
