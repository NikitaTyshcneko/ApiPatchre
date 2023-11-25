import os

params = {
    "apikey": os.getenv('MARVEL_API_KEY'),
    'ts': os.getenv('TS'),
    "hash": os.getenv('HASH')
}

base_url = "http://gateway.marvel.com/v1/public/characters"
