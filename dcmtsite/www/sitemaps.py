from django.contrib import sitemaps
from django.urls import reverse
from .models import Person

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main', 'research', 'publications', 'people', 'conferences', 'grants', 'contacts', 
                 'main_en', 'research_en', 'publications_en', 'people_en', 'conferences_en', 'grants_en', 'contacts_en', ]

    def location(self, item):
        return reverse(item)

        
class PersonSitemapRu(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Person.objects.all()

        
class PersonSitemapEn(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Person.objects.all()
        
    def location(self, item):    
        return "en/people/%s" % item.slug   