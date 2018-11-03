from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Airport

def index(request):
    return render(request, 'index.html', {})

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
