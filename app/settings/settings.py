import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('', '.env')
load_dotenv(dotenv_path=env_path)

# Remove the commas at the end of each line
name = os.getenv('DBNAME')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOSTNAME')
port = os.getenv('PORT')

# Construct the DATABASE_URL
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{name}"