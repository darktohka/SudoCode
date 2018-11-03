from django.core.management.base import BaseCommand, CommandError
from sudocode.models import Airport
import requests

class Command(BaseCommand):
    help = 'Reloads all airports'

    def handle(self, *args, **options):
        Airport.objects.all().delete()
        airports = requests.get('https://raw.githubusercontent.com/mwgg/Airports/master/airports.json', headers={'User-Agent': 'Mozilla/5.0'}).json()

        for key, obj in airports.items():
            if not obj['name'] or not obj['city'] or not obj['iata'] or obj['iata'].isdigit():
                continue

            airport = Airport()
            airport.code = obj['iata'].strip()
            airport.name = obj['name'].strip()
            airport.city = obj['city'].strip()
            airport.latitude = float(obj.get('lat', 0))
            airport.longitude = float(obj.get('lon', 0))
            airport.country = obj['country'].strip()
            airport.save()

        print('Added {0} airports.'.format(Airport.objects.count()))
