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
	url(r'^scientists/fortova$', views.fortova),
	url(r'^scientists/shepelev1$', views.shepelev),
#	url(r'^scientists/shepelev$', views.researcher(slug='shepelev'),
	url(r'^scientists/?P<slug>a-z$', views.researcher(researcher_slug=slug), 
	url(r'^robots.txt$', views.robots_txt),
]