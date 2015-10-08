from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # TODO This was not syntactically valid
    # url(r'^$', views.),
]
