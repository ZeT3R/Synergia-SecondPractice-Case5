from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    location = Column(String)  # Местоположение
    image_url = Column(String) # Изображение
    cost = Column(Float)       # Стоимость
    description = Column(String)
