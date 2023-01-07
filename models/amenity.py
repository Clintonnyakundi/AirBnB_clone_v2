#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from models.place import place_amenity



class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    place_amenities = relationship("Place", secondary=place_amenity)
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
