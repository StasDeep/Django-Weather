# -*- coding: utf-8 -*-
import json
import urllib2
from BeautifulSoup import BeautifulSoup


def create_cities_fixture(codes):
    """Create fixture for filling weather.City table.
     
    Args:
        codes (list): list with 2-symbol strings, representing country codes.
    """
    # city.list.json is ~30 Mb, so it's better to download it from here:
    # http://bulk.openweathermap.org/sample/city.list.json.gz
    with open('city.list.json', 'r') as infile:
        cities = json.load(infile)

    new_cities = []
    for city in cities:
        if not city['country'] in codes:
            continue

        new_cities.append(dict(
            pk=city['id'],
            model='weather.City',
            fields=dict(
                name=city['name'],
                country=city['country']
            )
        ))

    with open('cities.json', 'w') as outfile:
        json.dump(new_cities, outfile)


def create_countries_fixture():
    """Create fixture for filling weather.Country table.
    
    Returns:
         list: codes of 247 countries as 2-symbol strings.
    """
    url = 'http://www.nationsonline.org/oneworld/country_code_list.htm'
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    tbody = soup.find('table', id='codelist')

    countries = []
    for row in tbody.findAll('tr')[2:]:
        cols = row.findAll('td')
        countries.append(dict(
            pk=cols[2].text,
            model='weather.Country',
            fields=dict(
                name=cols[1].text
            )
        ))

    with open('countries.json', 'w') as outfile:
        json.dump(countries, outfile)

    return [country['pk'] for country in countries]


def main():
    codes = create_countries_fixture()
    create_cities_fixture(codes)

if __name__ == '__main__':
    main()
