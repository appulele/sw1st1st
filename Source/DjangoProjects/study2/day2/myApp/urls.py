from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('views',
    url(r'^list/$', 'list', name='list'),
)

# urlpatterns = [
# url(r'^$', views.get_name, name='index0'),
# url(r'^$/', views.get_name, name='index1'),
# url(r'^your-name/', views.get_name, name='index2'),


# ]