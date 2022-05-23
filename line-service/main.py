from sys import api_version
import json
import requests

from Game import Game
import os

sport = 'baseball_mlb'
regions = 'us'
markets = "spreads,totals"
api_key =os.environ.get('ODDS_API_KEY')
url = str.format("https://api.the-odds-api.com/v4/sports/{}/odds/?apiKey={}&regions={}&markets={}", sport, api_key, regions, markets)
# url = str.format("https://api.the-odds-api.com/v4/sports/?apiKey={}", api_key)
# url = str.format("https://api.the-odds-api.com/v4/sports/baseball_mlb/scores/?daysFrom=1&apiKey={}", api_key)
r = requests.get(url)
lines = r.json()

print(api_key)
# mock = open('mockresp.json')
# lines = json.load(mock)


for gameDto in lines:
    game = Game(gameDto) 



print(game)

