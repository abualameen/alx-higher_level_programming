#!/usr/bin/python3
"""
th:s module is the module that creates the states column in the database


"""


from urllib.parse import quote_plus
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()


class State(Base):
    """
    this class is a class that represent the States column in the data base

    """
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, autoincrement=True,
        nullable=False, unique=True
    )
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    encoded_password = quote_plus(sys.argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], encoded_password, sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
