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
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        a,
        b,
        c),
        pool_pre_ping=True)
    Base.metadata.create_all(en)

    session = sessionmaker(bind=en)
    s = session()

    for state in s.query(State).filter(State.name.like('%a%')):
        print(f"{state.id}: {state.name}")
