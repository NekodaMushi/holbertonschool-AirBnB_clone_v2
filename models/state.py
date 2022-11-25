#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
""" `getenv` to determine in which storage type we are
by scanning the HBNB_TYPE_STORAGE"""


class State(BaseModel, Base):
    """
    State class
    Establish a relationship with the class City
    """
    if models.storage_type == 'db':
        """ db ==>  means let's go for SQLAlchemy logic"""
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

    if models.storage_type != 'db':
        @property
        def cities(self):
            """
            Getter - returns the list of City instances
            with state_id == State.id
            FileStorage relationship between State and City
            """
            cities_list = []
            all_cities = models.storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
