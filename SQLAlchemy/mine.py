from sqlalchemy import create_engine
DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost/alchemy_db'
engine = create_engine(DATABASE_URL)