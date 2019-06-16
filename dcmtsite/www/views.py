from django.shortcuts import render
from .models import Person, Paper
from datetime import date

# Create your views here.

def index(request):
    people = Person.objects.all().order_by('family_name')
    # return render(request, 'index.html')
    return render(request, 'index.html', {'people': people})

def research(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'research.html', {'people': people})
	
def publications(request):
    people = Person.objects.all().order_by('family_name')
    year_oldest = 2000
    year_cur = date.today().year
    years = range(year_oldest, year_cur+1)
    articles = Paper.objects.filter(type='ART')
    conf_procs = Paper.objects.filter(type='CPR')
    monos = Paper.objects.filter(type='MNG')
    preprints = Paper.objects.filter(type='PPR')
    other = Paper.objects.filter(type='OTH')	
    context = {'people': people, 
               'years': years,
               'articles': articles,
               'conf_procs': conf_procs, 
               'monos': monos, 
               'preprints': preprints,
               'other': other}
    return render(request, 'publications.html', context)

def scientists(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'scientists.html', {'people': people})		
	
def conferences(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'conferences.html', {'people': people})	
	
def grants(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'grants.html', {'people': people})

def contacts(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'contacts.html', {'people': people})

def robots_txt(request):
	return render(request, 'robots.txt')	
	
# Hardcoded for the prototype 
# TODO: parametric links with 'slug' parameter
def fortova(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'fortova.html', {'people': people})
	
def shepelev(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'shepelev.html', {'people': people})

	
	
	
	