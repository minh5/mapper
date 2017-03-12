from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
     url(r'^admin/', admin.site.urls),
    # custom
    url(r'^', include("mapper.data_file.urls", namespace='data_file')),
    url(r'^', include("mapper.map.urls", namespace='map'))
]
