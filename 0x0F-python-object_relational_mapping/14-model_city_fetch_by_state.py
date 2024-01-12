#!/usr/bin/python3
"""Start link class to table in database"""

from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id)
    for c, s in result:
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
