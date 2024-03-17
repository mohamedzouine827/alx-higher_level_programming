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
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_modify = session.query(State).filter_by(id=2).first()
    if state_to_modify:
        state_to_modify.name = 'New Mexico'
        session.commit()
        print(f"Modified ")
    else:
        print("not found ")
