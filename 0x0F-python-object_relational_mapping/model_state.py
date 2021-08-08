#!/usr/bin/python3
'''python file that contains the class definition of a State'''

# Import the module of clase base
from sqlalchemy.ext.declarative import declarative_base
# import objects type colum to create tha atributes of the class
from sqlalchemy import Column
# import the data types with which we are going to work in the columns
from sqlalchemy import Integer, String

# Create a instance of the main Base class.
Base = declarative_base()


# Model the State table
class State(Base):
    ''' Class definition of a State table'''
    # set table name
    __tablename__ = 'states'
    # set the atributes of the class (columns name)
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
