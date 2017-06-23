from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    family_name = models.CharField(max_length=40)
    degree = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    photo = models.CharField(max_length=256)
	
    def __str__(self):
        return self.name[0] + '.' + self.patronymic[0] + '. ' + self.family_name
	
class Paper(models.Model):
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
	
	title = models.CharField(max_length=256)
	dcmt_author_1 = models.CharField(max_length=40)
	dcmt_author_2 = models.CharField(max_length=40, blank=True)
	dcmt_author_3 = models.CharField(max_length=40, blank=True)
	dcmt_author_4 = models.CharField(max_length=40, blank=True)
	dcmt_author_5 = models.CharField(max_length=40, blank=True)
	dcmt_author_6 = models.CharField(max_length=40, blank=True)
	dcmt_author_7 = models.CharField(max_length=40, blank=True)
	dcmt_author_8 = models.CharField(max_length=40, blank=True)
	year = models.IntegerField()
	link = models.CharField(max_length=256, blank=True)
	type = models.CharField(max_length=3, choices = TYPE_CHOICES, default = ARTICLE)
    
	def __str__(self):
	    return self.title
	