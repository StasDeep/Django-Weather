# QWeather
Django training project to show current weather in the city.

## Installation

Install dependencies:
```
$ pip install -r requirements.txt
```

Set up database schema:
```
$ python manage.py migrate
```

Initialize Country table:
```
$ python manage.py loaddata countries
```

Initialize City table (takes 2-3 minutes, as there are ~210.000 records):
```
$ python manage.py loaddata cities
```

## Running

Start Django server:
```
$ python manage.py runserver localhost:8000
```

Go to http://localhost:8000/ and start using QWeather!
