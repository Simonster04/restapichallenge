#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Pets(BaseModel, Base):
    """Representation of Pets """
    if models.storage_t == 'db':
        __tablename__ = 'pets'
        name = Column(String(128), nullable=False)
        age = Column(Integer())
        color = Column(String(128))
        owner_id = Column(String(60), ForeignKey("owner.id"), nullable=False, index=True)
        owner = relationship("Owner", backref="pets", cascade="all, delete", foreign_keys=[owner_id])
    else:
        name = ""
        age = 0
        color = ""
    def __init__(self, *args, **kwargs):
        """initializes Pets"""
        super().__init__(*args, **kwargs)
