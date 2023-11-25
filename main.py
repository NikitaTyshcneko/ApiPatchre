from app.getdata import add_marvel_characters_to_db
from app.utils import base_url, params

if __name__ == '__main__':
    add_marvel_characters_to_db(base_url, params)

