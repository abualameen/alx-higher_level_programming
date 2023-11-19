#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects, contained in the
database hbtn_0e_101_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from urllib.parse import quote_plus


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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()