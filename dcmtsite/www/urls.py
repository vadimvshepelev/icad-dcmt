from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^$', views.index),
	url(r'^research/$', views.research),
	url(r'^publications/$', views.publications),
	url(r'^conferences/$', views.conferences),
	url(r'^grants/$', views.grants),
	url(r'^contacts/$', views.contacts),
	url(r'^scientists/$', views.scientists),
	url(r'^scientists/(?P<researcher_slug>[a-z]+)$', views.researcher), 
	url(r'^robots.txt$', views.robots_txt),
]