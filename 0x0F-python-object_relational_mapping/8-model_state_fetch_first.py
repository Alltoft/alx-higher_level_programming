#!/usr/bin/python3
"""
Define a State class
that inherits from sqlalchemy Base
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).first()

    if result is None:
        print("Nothing")
    else:
        print('{}: {}'.format(result.id, result.name))
