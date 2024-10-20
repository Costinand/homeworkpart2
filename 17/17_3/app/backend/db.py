from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///taskmanager.db", echo= True) # содание привязки с базой данных

SessionLocal = sessionmaker(bind=engine) # для создания сессии используется привязка engine

class Base(DeclarativeBase): # Базовый класс, на основе которого будут строиться таблицы
    pass
