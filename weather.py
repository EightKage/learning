import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name 
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()


    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=6c0648b6631ed23a65df107a7fdfbc1e")


        except:
            print("No Internet buddy ")


        self.response_json = response.json()

        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        print(f"In {self.name} its about {self.temp} C")
        print(f"Todays highs was {self.temp_max} C")
        print(f"The current low temprature for today was {self.temp_min} C")
        


my_city = City("Tokyo", 36.2048, -138.2529)
my_city.temp_print()

vaca_city = City("Abuja", 9.0563, -7.4985)
vaca_city.temp_print()