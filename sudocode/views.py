from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Airport
from . import utils
import time

def index(request):
    return render(request, 'index.html', {})

def search(request):
    if request.method != 'POST' or 'from' not in request.POST or 'to' not in request.POST or 'start' not in request.POST or 'end' not in request.POST:
        return HttpResponseRedirect('/')

    try:
        from_airport = Airport.objects.get(code__iexact=request.POST['from']).name
        to_airport = Airport.objects.get(code__iexact=request.POST['to']).name
        from_date = int(request.POST['start'])
        to_date = int(request.POST['end'])
    except:
        return HttpResponseRedirect('/')

    flights = utils.search_flights(from_airport, to_airport, from_date, to_date)
    return render(request, 'index.html', {'showWarning': True, 'flights': flights})

def airport_ajax(request):
    if 'term' not in request.GET:
        return JsonResponse({})

    term = request.GET['term']

    if len(term) == 3 and term.upper() == term:
        airports = Airport.objects.filter(code__iexact=term)[:10]
    else:
        airports = Airport.objects.filter(Q(code__iexact=term) | Q(name__icontains=term) | Q(city__icontains=term))[:10]

    values = [{'id': airport.code, 'value': '%s - %s (%s)' % (airport.city, airport.name, airport.code)} for airport in airports]
    values = sorted(values, key=lambda x: x['value'])

    return JsonResponse(values, safe=False)
