#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import getenv
import models

if getenv("HBNB_TYPE_STORAGE") == "db":
    class User(BaseModel, Base):
        """Representation of a user """
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place",
                            backref="user",
                            cascade="delete")
        reviews = relationship("Review",
                            backref="user",
                            cascade="delete")
else:
    class User(BaseModel):
        """Representation of a user """
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        
