#!/usr/bin/python3
"""Model state """


from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    en = create_engine('mysql+mysqldb://{}:{}@localhost:3066/{}'.format(
        a,
        b,
        c),
        pool_pre_ping=True)
    nameFounded = sys.argv[4]

    session = sessionmaker(bind=en)
    s = session()

    newSate = State(name="Louisiana")
    s.add(newSate)
    s.commit()

    length = s.query(State).order_by(State.id)
    print(f"{len(length)}")
