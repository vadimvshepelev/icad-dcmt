from django.shortcuts import render
from .models import Person, Paper

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
    publications = Paper.objects.all()
    articles = Paper.objects.filter(type='ART')
    conf_proc = Paper.objects.filter(type='CPR')	
    return render(request, 'publications.html', {'people': people, 'articles': articles, 'conf_proc': conf_proc})




