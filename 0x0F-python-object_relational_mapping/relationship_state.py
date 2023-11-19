#!/usr/bin/python3
"""
This module creates the class State with some attributes using SQLAlchemy
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """
    THIS IS CLASS STATE
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")
