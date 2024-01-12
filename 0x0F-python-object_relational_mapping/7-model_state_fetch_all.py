#!/usr/bin/python3
"""Start link class to table in database"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format('alo', 'Emran', 'hbtn_0e_6_usa'))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    for r in result:
        print('{}: {}'.format(r.id, r.name))
