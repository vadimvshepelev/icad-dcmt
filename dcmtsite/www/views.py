from django.shortcuts import render
from .models import Person, Paper
from datetime import date

# Create your views here.

def index(request):
    people = Person.objects.all()
    # return render(request, 'index.html')
    return render(request, 'index.html', {'people': people})

def research(request):
    people = Person.objects.all()
    return render(request, 'research.html', {'people': people})
	
def publications(request):
    people = Person.objects.all()
    year_oldest = 2000
    year_cur = date.today().year
    years = range(year_oldest, year_cur)
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




