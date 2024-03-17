#!/usr/bin/python3
"""Module to define a class State"""


import sqlalchemy as sql
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """this pycodestyle is killing me"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
