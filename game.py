import requests
from bs4 import BeautifulSoup

class Game:
    
    def __init__(self):
        game = requests.get('https://www.dragonsofmugloar.com/api/game').json()
        self.gameId = str(game['gameId'])

        self.attack = game['knight']['attack']
        self.armor = game['knight']['armor']
        self.agility = game['knight']['agility']
        self.endurance = game['knight']['endurance']

        weather_xml = requests.get('https://www.dragonsofmugloar.com/weather/api/report/' + self.gameId).text
        self.weather_code = BeautifulSoup(weather_xml, features="html5lib").code.get_text()

        print('Started game: ', game, ', Weather: ', self.weather_code)

    def submit(self, dragon):
        result = requests.put('https://www.dragonsofmugloar.com/api/game/' + self.gameId + '/solution', json={'dragon': dragon}).json()
        return result['status']

    def get_encoded_weather_representation(self):
        return {
            'FUNDEFINEDG': [1, 0, 0, 0, 0],
            'HVA': [0, 1, 0, 0, 0],
            'NMR': [0, 0, 1, 0, 0],
            'SRO': [0, 0, 0, 1, 0],
            'T E': [0, 0, 0, 0, 1],
        }[self.weather_code]