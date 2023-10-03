from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@db/postgres'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = sessionmaker(bind=engine)
Base = declarative_base()

from database import models


def get_db():
    db = session()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()