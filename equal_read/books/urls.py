from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search_books, name='search'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]
