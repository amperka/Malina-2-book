import requests
import json

url = 'http://api.openweathermap.org/data/2.5/forecast'

payload = {
    'lat': 'широта_твоего_города',
    'lon': 'долгота_твоего_города',
    'units': 'metric',
    'appid': 'твой_ключ',
}

res = requests.get(url, params=payload)
data = json.loads(res.text)

weather = data['list'][0]


def pars_weather(weatherType, timeRange, measurementUnits):
    if (weatherType in weather) and (
        timeRange in weather[weatherType].keys()
    ):
        print(
            weatherType,
            ': ',
            weather[weatherType][timeRange],
            measurementUnits,
        )
    else:
        print(weatherType, ': ', 'none')


pars_weather('clouds', 'all', '%')
pars_weather('rain', '3h', 'mm')
pars_weather('snow', '3h', 'mm')
print('temp:', weather['main']['temp'], 'C')
