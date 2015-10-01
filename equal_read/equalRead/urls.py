from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index$', views.home),
    url(r'^$', views.),
]