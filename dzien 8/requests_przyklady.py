# pip install requests
import sys
form datacalsses import dataclass
import requests

# resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/")
# print(resp.status_code)
# print(resp.content)
# for currency in resp.json()[0]["rates"]:
#    print(currency["currency"], currency ["mid"])

# ID, pogoda, cisnienie,
dane = []
id = []

@dataclass
class Weather:
    name: str



def get_location_id(location_name):
    query_url = "https://www.metaweather.com/api/location/search/?query=" + location name
    resp =requests.get(query_url)
    return resp.json()[0]["woeid"]
def get_location_weather(location_id):
    query_url = (f"https://www.metaweather.com/api/location" + location





resp = requests.get("https://www.metaweather.com/api/location/523920/")
for id in resp.json():
    print(id["id"], id)
