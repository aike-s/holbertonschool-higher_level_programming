#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

import sys
from model_city import City
from model_state import Base, State

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]

    engine = create_engine('mysql+mysqldb://{}:@localhost:3306/{}'.format(
        user, data_base), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    """ In city will be saved every object of this class """
    for city in session.query(City).order_by(City.id).all():
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))

    session.close()
