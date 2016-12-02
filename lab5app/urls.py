from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.navig, name='navigate'),
    url(r'^show_new/', views.show_new, name='show_new'),
    url(r'^show_all/', views.show_all, name='show_all'),
]