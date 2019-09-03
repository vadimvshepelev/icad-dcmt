from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps
from django.conf import settings
import django.views.static

urlpatterns = [ 
    url(r'^$', views.index, name='main'),
	url(r'^research/$', views.research, name='research'),
	url(r'^publications/$', views.publications, name='publications'),
	url(r'^conferences/$', views.conferences, name='conferences'),
	url(r'^grants/$', views.grants, name='grants'),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^people/$', views.people, name='people'),
	url(r'^people/(?P<researcher_slug>[a-z]+)$', views.researcher), 
    url(r'^en/$', views.index_en, name='main_en'),
    url(r'^en/research/$', views.research_en, name='research_en'),
	url(r'^en/publications/$', views.publications_en, name='publications_en'),
	url(r'^en/conferences/$', views.conferences_en, name='conferences_en'),
	url(r'^en/grants/$', views.grants_en, name='grants_en'),
	url(r'^en/contacts/$', views.contacts_en, name='contacts_en'),
	url(r'^en/people/$', views.people_en, name='people_en'),
	url(r'^en/people/(?P<researcher_slug>[a-z]+)$', views.researcher_en), 
	url(r'^robots.txt$', views.robots_txt),
    #url(r'^robots.txt$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^robots.txt$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'path': "robots.txt"}),
    url(r'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),    
]