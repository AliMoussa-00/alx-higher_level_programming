#!/usr/bin/python3
"""
a script that 'adds' the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sys import argv
from model_state import Base, State


def insertData_to_db(user, pw, db_name, obj):
    """Inserting to DB"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            session.add(obj)

            state = session.query(State).filter(State.name == obj.name).first()
            print(state.id)

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

        obj = State(name="Louisiana")

        insertData_to_db(user, pw, db_name, obj)
