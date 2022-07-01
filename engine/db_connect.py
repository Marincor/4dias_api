import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_MIGRATION_URL= os.getenv("DATABASE_MIGRATION_URL")

engine = create_engine(f'postgresql+psycopg2://{DATABASE_MIGRATION_URL}', client_encoding='utf8', implicit_returning=True)

