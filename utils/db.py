import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
from utils.models import Temperature

load_dotenv()

DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def load_temperature_data(start_date=None, end_date=None):
    query = select(Temperature).order_by(Temperature.date)

    if start_date:
        query = query.where(Temperature.date >= start_date)
    if end_date:
        query = query.where(Temperature.date <= end_date)

    with SessionLocal() as session:
        temps = session.scalars(query).all()

    return [
        {
            "date": t.date,
            "avgtemp_c": t.avgtemp_c,
            "mintemp_c": t.mintemp_c,
            "maxtemp_c": t.maxtemp_c,
        }
        for t in temps
    ]


def get_temperature_date_bounds():
    query = select(func.min(Temperature.date), func.max(Temperature.date))

    with SessionLocal() as session:
        min_date, max_date = session.execute(query).one()

    return min_date, max_date


   