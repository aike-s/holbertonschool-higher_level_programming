#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

import sys
from model_state import Base, State

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]
    search_state = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, password, data_base), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    state = session.query(State).order_by(State.id).all()

    for obj in state:
        if search_state == obj.name:
            print(obj.id)
            found = True

    if found is False:
        print("Not found")

    session.close()
