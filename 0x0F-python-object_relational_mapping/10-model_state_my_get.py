#!/usr/bin/python3
'''Script that prints the first State object from the database
hbtn_0e_6_usa'''

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
    # make the query and print data
    row = session.query(State).filter(State.name == sys.argv[4]).first()
    if row:
        print("{}".format(row.id))
    else:
        print('Not found')
    session.close()
