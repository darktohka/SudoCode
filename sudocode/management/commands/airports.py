from django.core.management.base import BaseCommand, CommandError
from sudocode.models import Airport
import requests

class Command(BaseCommand):
    help = 'Reloads all airports'

    def handle(self, *args, **options):
        Airport.objects.all().delete()
        airports = requests.get('https://raw.githubusercontent.com/jbrooksuk/JSON-Airports/master/airports.json', headers={'User-Agent': 'Mozilla/5.0'}).json()

        for obj in airports:
            if obj['type'] != 'airport' or not obj['name']:
                continue

            airport = Airport()
            airport.code = obj['iata']
            airport.iso_code = obj['iso']
            airport.name = obj['name']
            airport.latitude = float(obj.get('lat', 0))
            airport.longitude = float(obj.get('lon', 0))
            airport.continent = obj['continent']
            airport.save()

        print('Added {0} airports.'.format(Airport.objects.count()))
