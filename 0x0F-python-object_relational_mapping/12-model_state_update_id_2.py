#!/usr/bin/python3
"""Start link class to table in database"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter_by(id=2).first()

    if result:
        result.name = 'New Mexico'

    session.commit()
