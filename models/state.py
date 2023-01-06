#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascad="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """
            returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            related = []
            cities = storage.all(City)
            for city in cities:
                if city.state_id == self.id:
                    related.append(city)
            return (related)
