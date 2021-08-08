#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

import sys
from model_state import State

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, password, data_base), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """ In state will be saved every object of this class """
    for state in session.query(State).order_by(State.id).all():
        print("{:d}: {}".format(state.id, state.name))

    session.close()
