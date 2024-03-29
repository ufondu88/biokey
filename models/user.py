from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates
from setup import Base

class User(Base):
  __tablename__ = "users"

  id = Column("id", Integer, primary_key=True, autoincrement="auto")
  first_name = Column("first_name", String(50), nullable=False)
  last_name = Column("last_name", String(50), nullable=False)
  age = Column("age", Integer, nullable=False)

  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def __repr__(self):
    return f"{self.id}: {self.first_name} {self.last_name} ({self.age})"
  
  @validates('first_name', 'last_name')
  def validate_first_name(self, key, value):
    if not value:
        raise ValueError(f'{key} cannot be empty.')

    if len(value) < 2:
        raise ValueError(f'{key} must be at least 2 characters long.')

    return value

  @validates('age')
  def validate_age(self, key, value):
    if not isinstance(value, int):
       raise ValueError('age must be a number')

    if value < 0:
        raise ValueError('age cannot be negative')

    return value

