#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String
from sqlalchemy.orm import relationship
from models.place import Place


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    ''' deleted this: secondary=place_amenity '''
    """ commenting out code from task 10 to see if we get green checks again
    place_amenities = relationship("Place", secondary=Place.place_amenity,
                                    backref='amenities')
    """
