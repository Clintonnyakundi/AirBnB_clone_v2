#!/usr/bin/python3
""" Review Class File """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """ Define Review Class
        __tablename__: reviews
        text: Column String(1024) can't be null
        place_id: Column String(60) ForeignKey to places.id can't be null
        user_id: Column String(60) ForeignKey to users.id can't be null
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
