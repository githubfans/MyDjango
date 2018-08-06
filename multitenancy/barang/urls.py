from django.conf.urls import url
from django.contrib import admin

from barang import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^admin/', admin.site.urls),
]
