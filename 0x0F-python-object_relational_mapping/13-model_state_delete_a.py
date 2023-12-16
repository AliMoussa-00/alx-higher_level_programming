#!/usr/bin/python3
"""
a script that deletes all 'State objects' with a 'name'
containing the letter 'a' from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sys import argv
from model_state import Base, State


def delete_Data_from_db(user, pw, db_name):
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:

            states = session.query(State).filter(State.name.like("%a%")).all()

            if states:
                for state in states:
                    session.delete(state)

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

        delete_Data_from_db(user, pw, db_name)
