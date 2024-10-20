from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from user import *



class Task(Base):
    __tablename__ = "tasks"
    __table_ars__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)


    user = relationship('User', back_populates= 'tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))

''' Несколько часов бился с проблемой вывода таблиц. Работает только если вызов делать из модуля task. При этом импорт 
 можно сделать только модуля user для модуля task ,при чём весь - иначе ошибка. Отдельно импортировать класс User не
  получается. Попытка импорта task в user также приводит к ошибке. Убирать строчки с принтом из user также нельзя 
  . Вобщем, делал все по инструкции,а в результате как шаман с бубном пытался заставить работать эту махину. 
  И конспект, написанный один в один с лекции выводит только половину таблицы. 
  Вывод: или лекция написана для какой-то более ранней версии фраймворков или в ней что-то не досказано .'''