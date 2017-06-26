from django.shortcuts import render
from .models import Person

# Create your views here.

def index(request):
    people = Person.objects.all()
    # return render(request, 'index.html')
    return render(request, 'index.html', {'people': people})

def research(request):
    return render(request, 'research.html')
