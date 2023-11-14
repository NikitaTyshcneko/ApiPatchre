import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

name = os.getenv('DBNAME'),
user = os.getenv('USER'),
password = os.getenv('PASSWORD'),
host = os.getenv('HOSTNAME'),
port = os.getenv('PORT')
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{name}"