#!/usr/bin/python
""" holds class Owner"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Owner(BaseModel, Base):
    """Representation of a Owner """
    if models.storage_t == 'db':
        __tablename__ = 'owner'
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes Owner"""
        super().__init__(*args, **kwargs)
