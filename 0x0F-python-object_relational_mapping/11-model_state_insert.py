#!/usr/bin/python3
'''script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa'''

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
    # make the query
    object_to_add = State(name='Louisiana')
    # add user to stack
    session.add(object_to_add)
    # Confirm the changes on the data base
    session.commit()
    # print new onject
    new_object = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(new_object.id))
    session.close()
