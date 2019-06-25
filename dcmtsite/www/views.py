from django.shortcuts import render
from .models import Person, Paper
from datetime import date

# Create your views here

def index(request):
    # people = Person.objects.all().order_by('family_name')
    # return render(request, 'index.html')
    return render(request, 'index.html')

def research(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'research.html', {'people': people})
	
def publications(request):
    people = Person.objects.all().order_by('family_name')
    #year_oldest = 2000
    #year_cur = date.today().year
    #years = range(year_oldest, year_cur+1)
    papers = Paper.objects.all()
    context = {'people': people, 
               'papers': papers}
    return render(request, 'publications.html', context)

def people(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'people.html', {'people': people})		
	
def conferences(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'conferences.html', {'people': people})	
	
def grants(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'grants.html', {'people': people})

def contacts(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'contacts.html', {'people': people})

def researcher(request, researcher_slug):
    researcher = Person.objects.get(slug=researcher_slug)
    papers = Paper.objects.filter(dcmt_authors=researcher)
    context = {'researcher_slug': researcher_slug, 'researcher': researcher, 'papers': papers }
    return render(request, 'researcher_card.html', context)

def index_en(request):
    # people = Person.objects.all().order_by('family_name_en')    
    return render(request, 'index_en.html')

def research_en(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'research_en.html', {'people': people})
	
def publications_en(request):
    people = Person.objects.all().order_by('family_name')
    # year_oldest = 2000
    # year_cur = date.today().year
    # years = range(year_oldest, year_cur+1)
    papers = Paper.objects.all();
    # articles = Paper.objects.filter(type='ART')
    # conf_procs = Paper.objects.filter(type='CPR')
    # monos = Paper.objects.filter(type='MNG')
    # preprints = Paper.objects.filter(type='PPR')
    # other = Paper.objects.filter(type='OTH')	
    context = {'people': people,                
               'papers': papers}
    return render(request, 'publications_en.html', context)

def people_en(request):
    people = Person.objects.all().order_by('family_name_en')
    return render(request, 'people_en.html', {'people': people})		
	
def conferences_en(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'conferences_en.html', {'people': people})	
	
def grants_en(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'grants_en.html', {'people': people})

def contacts_en(request):
    people = Person.objects.all().order_by('family_name')
    return render(request, 'contacts_en.html', {'people': people})

def researcher_en(request, researcher_slug):
    researcher = Person.objects.get(slug=researcher_slug)
    papers = Paper.objects.filter(dcmt_authors=researcher)
    context = {'researcher_slug': researcher_slug, 'researcher': researcher, 'papers': papers }
    return render(request, 'researcher_card_en.html', context)


def robots_txt(request):
	return render(request, 'robots.txt', content_type='text/plain')	
    