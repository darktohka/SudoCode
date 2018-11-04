from bs4 import BeautifulSoup
import requests, delegator, datetime, os, sys

def get_month_day(millisecs):
    return datetime.datetime.fromtimestamp(millisecs).strftime('%B %d')

def find_flights(from_airport, to_airport, from_date, to_date):
    if sys.platform != 'linux2':
        return [{'link': 'https://google.com', 'name': 'Test', 'time': '2 hrs', 'money': '$210'}]

    from_date = get_month_day(from_date)
    to_date = get_month_day(to_date)
    search = 'Google Flights from %s to %s from %s to %s' % (from_airport, to_airport, from_date, to_date)

    link = 'https://www.google.com/search?q=%s&hl=en&gl=us' % '+'.join(search.split(' '))
    first = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(first.text, features='html.parser')
    link = 'https://www.google.com' + soup.find('div', style='display:block').find('a')['href']

    curl = "/bin/bash %s %s" % (os.path.join(os.getcwd(), "scrape.sh"), link)
    curl = delegator.run(curl)
    curl.block()

    soup = BeautifulSoup(curl.out, features='html.parser')
    planes = soup.find('div', {'class': 'flt-results'})

    if not planes:
        return []
    results = []

    for plane in planes.div.findAll('div'):
        link = plane.a['href']
        spans = plane.findAll('span')
        name = spans[3].text
        time = spans[4].text
        money = spans[7].text
        results.append({'link': link, 'name': name, 'time': time, 'money': money})

    return results

