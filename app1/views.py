from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def portfolio_view(request):
    about = About.objects.all()  # Fetch all About entry
    skills = Skills.objects.all()  # Fetch all skills
    projects = My_projects.objects.all()  # Fetch all projects
    contact = Contact.objects.last()  # Fetch the first Contact entry

    return render(request, 'index.html', {
        'about': about,
        'skills': skills,
        'projects': projects,
        'contact': contact,
    })