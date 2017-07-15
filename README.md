# QWeather
Django training project to show current weather in the city.

## Installation

Set up database schema:
```
$ python manage.py migrate
```

Initialize Country table:
```
$ python manage.py loaddata countries
```

Initialize City table (takes some time, as there are ~210.000 records):
```
$ python manage.py loaddata cities
```
