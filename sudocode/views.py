from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Airport

def index(request):
    return render(request, 'index.html', {})
