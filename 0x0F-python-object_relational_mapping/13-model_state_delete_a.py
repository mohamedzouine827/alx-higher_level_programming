#!/usr/bin/python3
"""prints the first state"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3066/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    deleted = State.name.like('%a%')
    state_to_delete = session.query(State).filter_by(deleted).delete()
    state_to_delete.commit()
