import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from app.db import engine
from app.models.models import Card

env_path = Path('', '.env')
load_dotenv(dotenv_path=env_path)


def add_marvel_characters_to_db(base_url, params):
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        character_data = response.json()

        if character_data['data']['count'] > 0:
            Session = sessionmaker(bind=engine)
            session = Session()
            session.bulk_save_objects(get_list_of_character(character_data['data']['results']))
            session.commit()
            session.close()
        else:
            print(f"No character found with the name")
    else:
        print(f"Error: {response.status_code} - {response.text}")


def get_list_of_character(character_data):
    characters_info_list = []

    for character in character_data:
        character_inf_for_db = Card(
            id=character['id'],
            name=character['name'],
            description=character['description'],
            resourceURI=character['resourceURI']
        )
        characters_info_list.append(character_inf_for_db)

    return characters_info_list
