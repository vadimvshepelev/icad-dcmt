from django.db import models


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
    date = models.DateField(auto_now_add=True, editable=True, blank=True)
    authors = models.TextField(max_length=256) 
    title = models.TextField(max_length=256)
    journal = models.TextField(max_length=256, verbose_name='Journal, Volume, Pages')
    dcmt_authors = models.ManyToManyField(Person);
    abs_link = models.CharField(max_length=256, blank=True)
    rinc_link = models.CharField(max_length=256, blank=True)
    scopus_link = models.CharField(max_length=256, blank=True)
    wos_link = models.CharField(max_length=256, blank=True)
    download_link = models.CharField(max_length=256, blank=True)
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
    type = models.CharField(max_length=3, choices = TYPE_CHOICES, default = ARTICLE)
    
    def __str__(self):
        words_list = self.authors.split()[:4] + ["..."] + self.title.split()[:4] 
        str = ' '.join(words_list) + "..."
        return str
