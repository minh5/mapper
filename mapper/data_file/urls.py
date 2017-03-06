from django.conf.urls import include, url
from django.contrib import admin

from .views import MapView

urlpatterns = [
    url(r'^$', MapView.as_view(), name='data_file')
    ]
