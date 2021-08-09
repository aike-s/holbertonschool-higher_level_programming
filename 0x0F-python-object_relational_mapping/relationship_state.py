#!/usr/bin/python3
"""
Class definition of a State and an instance Base
"""

from relationship_city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Initialization of table/class State """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
