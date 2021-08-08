#!/usr/bin/python3
"""
Adds the State object “Louisiana”
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

import sys
from model_state import Base, State

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, password, data_base), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    name_state = 'Louisiana'
    session.add(State(name=name_state))
    session.commit()

    added_state = session.query(State).filter(State.name == name_state).first()

    print(added_state.id)

    session.close()
