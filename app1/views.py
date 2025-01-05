from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    projects = My_projects.objects.all()
    skills = Skills.objects.all()
    return render(request, 'index.html', {'projects': projects, 'skills': skills})
