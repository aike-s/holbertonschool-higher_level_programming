#!/usr/bin/python3
"""
Changes the name of a State object
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

import sys
from model_state import Base, State

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, password, data_base), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        if state.id == 2:
            state.name = "New Mexico"
            session.commit()

    session.close()
