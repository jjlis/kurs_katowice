import sys
from dataclasses import dataclass
import requests
import tkinter


# można by też uzyć namedtuple z collections

@dataclass
class Weather:
    name: str
    temp: float
    humidity: float
    air_pressure: float

    def raport(self):
        return f"""Pogoda w {self.name}:
temperatura: {self.temp}
wilgotność: {self.humidity}
ciśnienie: {self.air_pressure}
"""


def get_location_id(location_name):
    query_url = "https://www.metaweather.com/api/location/search/?query=" + location_name
    resp = requests.get(query_url)
    return resp.json()[0]["woeid"]


def get_location_weather(location_id):
    query_url = f"https://www.metaweather.com/api/location/{location_id}/"
    resp = requests.get(query_url)
    location_name = resp.json()['title']
    data = resp.json()['consolidated_weather'][0]
    weather = Weather(
        name=location_name,
        temp=data["the_temp"],
        humidity=data["humidity"],
        air_pressure=data["air_pressure"]
    )
    return weather
def wyswietl():
    name = location_name.get()
    weather = Weather.get()

if __name__ == "__main__":
    print(sys.argv)
    location_name = sys.argv[1] if len(sys.argv) == 2 else "warsaw"
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    print(weather.raport())

root = tkinter.Tk()
label_a = tkinter.Label(master=root, text="name")
label_a.pack()
location_name = tkinter.Entry(master=root)
location_name.pack()
label_b = tkinter.Label(master=root, text="weather")
label_b.pack()
Weather = tkinter.Entry(master=root)
Weather.pack()
root.mainloop()