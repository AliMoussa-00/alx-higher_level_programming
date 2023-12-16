#!/usr/bin/python3
"""
file similar to model_state.py named model_city.py that
contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base


class City(Base):
    """Defining the City class"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id', ondelete='CASCADE'))
