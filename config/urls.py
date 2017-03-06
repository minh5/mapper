from django.conf.urls import include, url
from django.contrib import admin

from mapper.data_file import views
import config.settings as settings

urlpatterns = [
     url(r'^admin/', admin.site.urls),
    # custom
    url(r'^', include("mapper.data_file.urls"))
    # url(r'^map/', include("mapper.map.urls", namespace="map")),
]
