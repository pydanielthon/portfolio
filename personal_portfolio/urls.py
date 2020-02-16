from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    url(r'^$', home, name='home'),

]