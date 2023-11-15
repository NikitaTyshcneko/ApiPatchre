import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('', '.env')
load_dotenv(dotenv_path=env_path)


def get_marvel_character():
    base_url = "http://gateway.marvel.com/v1/public/characters"

    params = {
        "apikey": os.getenv('MARVEL_API_KEY'),
        'ts': os.getenv('TS'),
        "hash": os.getenv('HASH')
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        character_data = response.json()

        if character_data['data']['count'] > 0:
            characters_info_list = []
            for character in character_data['data']['results']:
                character_info = {
                    'id': character['id'],
                    'name': character['name'],
                    'description': character['description'],
                    'resourceURI': character['resourceURI']
                }
                characters_info_list.append(character_info)

            write_to_json_file(characters_info_list)

        else:
            print(f"No character found with the name")
    else:
        print(f"Error: {response.status_code} - {response.text}")


def write_to_json_file(character_info):
    filename = f"сharacter_info.json"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(character_info, file, ensure_ascii=False, indent=4)
    print(f"Character information saved to {filename}")
