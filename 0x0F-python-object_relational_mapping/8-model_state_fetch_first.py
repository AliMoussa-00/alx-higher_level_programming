#!/usr/bin/python3
"""
a script that prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from sys import argv
from model_state import Base, State


if __name__ == "__main__":

    if len(argv) >= 4:
        user = argv[1]
        pw = argv[2]
        db_name = argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).first()

        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

        session.close()
