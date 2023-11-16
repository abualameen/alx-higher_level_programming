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
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = quote_plus(sys.argv[2])
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    all_statewith_a = session.query(State).filter(State.name.like('%a%')).all()

    for state in  all_statewith_a:
        session.delete(state)

    session.commit()
    print("States with 'a' in the name deleted successfully")
    session.close()

