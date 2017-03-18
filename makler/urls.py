#!/usr/bin/python3
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from . import views

app_name = 'makler'
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^estate/(?P<estatename>(.*))$', views.estateDetail, name="estateDetail"),
    url(r'^gallery/(?P<specialname>(.*))/(?P<estatename>(.*))$', views.special, name="special"),
    url(r'^video/(?P<specialname>(.*))/(?P<estatename>(.*))$', views.specialv, name="specialv"),
    url(r'^grdriss/(?P<specialname>(.*))/(?P<estatename>(.*))$', views.specialg, name="specialg"),
    url(r'^person/', views.person, name="person"),
    url(r'^sell/', views.sell, name="sell"),
    url(r'^buy/', views.buy, name="buy"),
    url(r'^rating/', views.rating, name="rating"),
    url(r'^consulting/', views.consulting, name="consulting"),
    url(r'^onefamily/', views.one, name="one"),
    url(r'^whgeigen/', views.eigen, name="eigen"),
    url(r'^whgkapital/', views.kapital, name="kapital"),
    url(r'^morefamily/', views.more, name="more"),
    url(r'^plot/', views.plot, name="plot"),
    url(r'^business/', views.business, name="business"),
    url(r'^sold', views.sold, name="sold"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^impressum/', views.impressum, name="impressum"),
    url(r'^impressum/datenschutz/', views.datenschutz, name="datenschutz"),
    url(r'^impressum/agb/', views.agb, name="agb"),
    url(r'^impressum/geldwaesche/', views.geldwaesche, name="geldwaesche"),
    url(r'^impressum/verbraucherinfo/', views.verbraucherinfo, name="verbraucherinfo"),
    url(r'^danke/', views.danke, name="danke"),
    url(r'^thanks/', views.thanks, name="thanks"),
    url(r'^output/$', views.output, name="output"),
    url(r'^media/(?P<filename>.*)$', views.expose, name="expose"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
