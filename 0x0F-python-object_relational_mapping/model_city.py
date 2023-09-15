#!/usr/bin/python3
"""python file contains the class definition of a city """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class City(Base):
    """class definition of a City

    Args:
        Base (class): declarative base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id=Column(Integer, ForeignKey('States.id'))
