#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        """Representation of Amenity 
        Attributes:
        name: input name
        """
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary="place_amenities",
            backref="amenities"
            )
else:
    class Amenity(BaseModel):
        """Representation of Amenity 
        Attributes:
        name: input name
        """
        name = ""
