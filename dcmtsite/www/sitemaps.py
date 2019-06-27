from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main', 'research', 'publications', 'people', 'conferences', 'grants', 'contacts', 
                 'main_en', 'research_en', 'publications_en', 'people_en', 'conferences_en', 'grants_en', 'contacts_en', ]

    def location(self, item):
        return reverse(item)