from django.conf.urls import include, url
# from django.urls import path
# from multitenancy.views import HomeView
from django.contrib import admin

urlpatterns = [
    # path('', HomeView.as_view()),
    # path('admin/', admin.site.urls),


    # url('', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
]
