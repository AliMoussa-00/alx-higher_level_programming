#!/usr/bin/python3
"""
a script that prints the State object with the 'name' passed as argument
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from sys import argv
from model_state import Base, State


if __name__ == "__main__":

    if len(argv) >= 5:
        user = argv[1]
        pw = argv[2]
        db_name = argv[3]
        state_name = argv[4]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).filter(State.name == state_name).all()

        if states:
            for state in states:
                print(state.id)
        else:
            print("Nothing")

        session.close()
