# demo/urls.py
from django.conf.urls import url

from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.gdp_year,name='gdp_year')
   # url(r'^$', views.gdp_growth, name='gdp_growth')
]