from sqlalchemy import Column, Integer, String
from connection import Base

# para que sea unico -> unique = True

class Item(Base):
  __tablename__ = 'items'
  id = Column(Integer,primary_key = True, index = True)
  name = Column(String(20))
  lastname = Column(String(20))
  age = Column(Integer)

class Post(Base):
  __tablename__ = 'itemspost'
  id = Column(Integer,primary_key = True, index = True)
  age = Column(Integer)