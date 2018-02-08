from django.conf.urls import url
from . import views


app_name = 'photos'
urlpatterns = [
    url(r'^list/$', views.photo_list, name='photo_list'),   
    url(r'^(?P<pk>\d+)/$', views.photo_detail, name='photo_detail'),   
]
