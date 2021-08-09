#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
# Import class sessionmaker to create the relation between DB and APP
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Make the base of sessions
    Session = sessionmaker(engine)
    # instance of Session Class
    session = Session()
    # Make the query
    # states = session.query(State).all()
    # print data
    for row in session.query(State).order_by(State.id).all():
        print("{}: {}".format(row.id, row.name))
