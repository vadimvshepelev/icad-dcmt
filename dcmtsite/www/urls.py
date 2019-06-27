from django.conf.urls import url
from . import views
# from models import PersonSitemap, PersonSitemapEn, StaticSitemap
# from .models import StaticSitemap
# from .models import *
from django.contrib.sitemaps.views import sitemap
# from django.urls import path
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [ 
    url(r'^$', views.index, name='main'),
	url(r'^research/$', views.research, name='research'),
	url(r'^publications/$', views.publications),
	url(r'^conferences/$', views.conferences),
	url(r'^grants/$', views.grants),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^people/$', views.people),
	url(r'^people/(?P<researcher_slug>[a-z]+)$', views.researcher), 
    url(r'^en/$', views.index_en),
    url(r'^en/research/$', views.research_en),
	url(r'^en/publications/$', views.publications_en),
	url(r'^en/conferences/$', views.conferences_en),
	url(r'^en/grants/$', views.grants_en),
	url(r'^en/contacts/$', views.contacts_en),
	url(r'^en/people/$', views.people_en),
	url(r'^en/people/(?P<researcher_slug>[a-z]+)$', views.researcher_en), 
	url(r'^robots.txt$', views.robots_txt),
#    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

#sitemaps = {
#	'people': PersonSitemap,
#    'people_en': PersonSitemapEn,    
#	'static': StaticSitemap,
#}
