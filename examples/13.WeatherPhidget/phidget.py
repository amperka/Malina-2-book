import requests, json

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

#
#(1) Подключаем библиотеку requests для генерации запросов и json для обработки ответов.
#(3) В переменной url храним адрес сайта, к которому будем обращаться за информацией о погоде.
#(6-9) В переменную payload записываем пары ключ-значение: широта, долгота, единицы измерения и ключ API. Для примера широта и долгота московского офиса Амперки 55.7440 и 37.6568.
#(12) Производим запрос к сервису погоды (url) с заданными параметрами (payload). Ответ вернётся в формате JSON.
#(13) Функцией json.loads() преобразуем JSON к словарю.
#(17-28) Функция pars_weather проходится по словарю и, в зависимости от полученных параметров, выводит удобочитаемый прогноз погоды.
#(33) Выводим значение температуры.
#