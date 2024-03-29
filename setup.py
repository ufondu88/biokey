from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///database/db.sqlite", echo=True)
Session = sessionmaker(bind=engine)

def init_db():
  try:
    Base.metadata.create_all(bind=engine)
  except Exception as e:
    if "already exists" in str(e):
      print("Table already exists. Moving on...")
  
session = Session()