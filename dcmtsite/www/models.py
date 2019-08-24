from django.db import models
from django import datetime as dt


class Person(models.Model):
    name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    family_name = models.CharField(max_length=40)
    degree = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    photo = models.CharField(max_length=256)
    name_en = models.CharField(max_length=40, default='Name')
    patronymic_en = models.CharField(max_length=40, default='P.')
    family_name_en = models.CharField(max_length=40, default='Family Name')
    degree_en = models.CharField(max_length=40, default='Degree')
    position_en = models.CharField(max_length=40, default='Position')
	
    slug = models.SlugField()
    
    def __str__(self):
        return self.name[0] + '.' + self.patronymic[0] + '. ' + self.family_name 
	
    def __str_en__(self):
        return self.name_en[0] + '.' + self.patronymic_en[0] + '. ' + self.family_name_en 
        
    def get_absolute_url(self):
        return "/people/%s" % self.slug       
        
		
class Paper(models.Model):
    date = models.DateField(default=dt.date.today(), editable=True, blank=False)
    authors = models.TextField(max_length=256) 
    title = models.TextField(max_length=256)
    journal = models.TextField(max_length=256, verbose_name='Journal, Volume, Pages etc.')
    dcmt_authors = models.ManyToManyField(Person, verbose_name='Authors from DCM&T');
    abs_link = models.CharField(max_length=256, blank=True, verbose_name='Abstract URL')
    rinc_link = models.CharField(max_length=256, blank=True, verbose_name='RINC citing URL')
    scopus_link = models.CharField(max_length=256, blank=True, verbose_name='Scopus citing URL')
    wos_link = models.CharField(max_length=256, blank=True, verbose_name='Web of Science citing URL')
    download_link = models.CharField(max_length=256, blank=True, verbose_name='Download URL')
    ARTICLE = 'ART'
    CONF_PROC = 'CPR'
    MONOGRAPHY = 'MNG'
    PREPRINT = 'PPR'
    OTHER = 'OTH'
    TYPE_CHOICES = (
        (ARTICLE, 'article'),
        (CONF_PROC, 'conference proceeding'),
        (MONOGRAPHY, 'monography'),
         (PREPRINT, 'preprint'),
        (OTHER, 'other')
    )
    type = models.CharField(max_length=3, choices = TYPE_CHOICES, default = ARTICLE, verbose_name='Paper type')    
    
    def __str__(self):
        words_list = self.authors.split()[:4] + ["..."] + self.title.split()[:4] 
        str = ' '.join(words_list) + "..."
        return str
