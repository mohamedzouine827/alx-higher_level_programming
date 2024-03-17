#!/usr/bin/python3
"""prints the first state"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        a,
        b,
        c),
        pool_pre_ping=True)
    Base.metadata.create_all(en)

    session = sessionmaker(bind=en)
    s = session()
    myStates = s.query(State).order_by(State.id)
    if myStates:
        for state in myStates:
            print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
