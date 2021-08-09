#!/usr/bin/python3
'''Script that prints all City objects from the database hbtn_0e_14_usa '''
import sys
from model_state import Base, State
from model_city import City
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
    # print data
    for row in session.query(City).order_by(City.id).join(State)\
                      .all():
        print("{}: ({}) {}".format(row.state.name, row.id, row.name))
    session.close()
