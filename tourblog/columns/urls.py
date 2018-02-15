from django.conf.urls import url
from . import views


app_name = 'columns'
urlpatterns = [
    url(r'^list/$', views.column_list, name='column_list'),    
]
