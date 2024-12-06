import requests

api_key = "a58ba920f623f637f3947c16597fce58"

parameters = {
    "lat": 19.075983,
    "lon" : 72.877655
    ,"appid" :  api_key
}


response = requests.get(url = "http://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()

print(data)