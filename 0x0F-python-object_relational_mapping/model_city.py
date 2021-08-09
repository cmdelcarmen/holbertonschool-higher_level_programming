#!/usr/bin/python3
''' Defines class City that inherits from
Base '''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class City(Base):
    ''' Defines a City '''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
