"""duedueAnaly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from analysys.views import analy,index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index ,name="default"),
    url(r'^9', analy ,name="9"),
    url(r'^10', analy ,name="10"),
    url(r'^12', analy ,name="12"),
    url(r'^13', analy ,name="13"),
    url(r'^17', analy ,name="17"),
    url(r'^21', analy ,name="21"),
    url(r'^23', analy ,name="23"),
    url(r'^24', analy ,name="24"),
    url(r'^25', analy ,name="25"),
]
