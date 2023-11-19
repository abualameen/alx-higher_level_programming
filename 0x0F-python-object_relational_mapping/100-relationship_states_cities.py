#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa.
"""

from urllib.parse import quote_plus
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password>\
            <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = quote_plus(sys.argv[2])
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    california = State(name="California", cities=[City(name="San Francisco")])
    session.add(california)
    session.commit()
    session.close()
