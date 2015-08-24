from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^$', views.get_name, name='index0'),
url(r'^$/', views.get_name, name='index1'),
url(r'^your-name/', views.get_name, name='index2'),

]