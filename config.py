import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("FSTR_DB_HOST")
DB_PORT = os.getenv("FSTR_DB_PORT")
DB_NAME = os.getenv("FSTR_DB_NAME")
DB_USER = os.getenv("FSTR_DB_LOGIN")
DB_PASS = os.getenv("FSTR_DB_PASS")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
