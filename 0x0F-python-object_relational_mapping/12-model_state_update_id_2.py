#!/usr/bin/python3
"""
 a script that 'changes' the 'name' of a State object from the database
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sys import argv
from model_state import Base, State


def updateData_in_db(user, pw, db_name, state_id):
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:

            state = session.query(State).filter(State.id == state_id).first()

            if state:
                state.name = "New Mexico"

                session.commit()

        except SQLAlchemyError as e:
            # Rollback changes if an exception occurs
            session.rollback()
            print(e)

        session.close()

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":

    if len(argv) >= 4:
        user = argv[1]
        pw = argv[2]
        db_name = argv[3]

        updateData_in_db(user, pw, db_name, 2)
