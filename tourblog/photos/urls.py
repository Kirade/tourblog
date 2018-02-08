from django.conf.urls import url
from . import views


app_name = 'photos'
urlpatterns = [
    url(r'^list/$', views.photo_list, name='photo_list'),   
    url(r'^new/$', views.photo_new, name='photo_new'),   
    url(r'^(?P<pk>\d+)/$', views.photo_detail, name='photo_detail'),   
    url(r'^(?P<pk>\d+)/edit/$', views.photo_edit, name='photo_edit'),   
    url(r'^(?P<pk>\d+)/delete/$', views.photo_delete, name='photo_delete'),   
    url(r'^comment/(?P<pk>\d+)/new/$', views.new_comment, name='new_comment'),   
]
