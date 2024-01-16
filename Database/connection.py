from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from decouple import config

DB_HOST = config('HOSTNAME')
DB_USER = config('USERNAME')
DB_PASSWORD = config('PASSWORD')
DB_PORT = config('PORT')
DB_DATABASE = config('DATABASE')


DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()