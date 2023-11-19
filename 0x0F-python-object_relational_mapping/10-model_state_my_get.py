#!/usr/bin/python3
"""
this model that lists all State objects from the database hbtn_0e_6_usa.
"""


from urllib.parse import quote_plus
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password>\
                <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = quote_plus(sys.argv[2])
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    result = session.query(State).filter(State.name == state_name).first()
    if result:
        print(result.id)
    else:
        print("Not found")
    session.close()
