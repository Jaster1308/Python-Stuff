import requests
import os

set omdb_key=f8a9f4d8

key = os.environ['omdb_key']

base_url = "http://www.omdbapi.com"
movies = input('What are we lookin for?')

params = {'apikey' : key, 't' : movies}
data = requests.get(base_url, params).json()

print(data)
print('Rating for this movie: ')
print(data(['Ratings'] [0] ['Value']))
