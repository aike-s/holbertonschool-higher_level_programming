#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

import sys
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]

    engine = create_engine('mysql+mysqldb://{}:@localhost:3306/{}'.format(
        user, data_base), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California", cities=[City(name="San Francisco")])

    session.add(state)

    session.commit()
    session.close()
