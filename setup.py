from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///database.db", echo=True)
Session = sessionmaker(bind=engine)


session = Session()