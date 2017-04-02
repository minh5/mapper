from django.conf.urls import include, url
from django.contrib import admin

from .models import DataFile
from .views import DataCreateView, DataDetailView

urlpatterns = [
    url(regex=r'^$',
        view=DataCreateView.as_view(model=DataFile, success_url="data_detail"),
        name='data_create'),
    url(
        regex=r'^columns',
        view=DataDetailView.as_view(),
        name='data-detail'),
    # url(r'^columns/', ColumnView.as_view(), name='column_list')
    ]
