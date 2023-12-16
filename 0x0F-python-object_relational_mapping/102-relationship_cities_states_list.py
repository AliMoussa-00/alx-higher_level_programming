#!/usr/bin/python3
"""
 a script that lists all City objects from the database hbtn_0e_101_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sys import argv
from relationship_state import Base, State
from relationship_city import City


def get_state_with_city(user, pw, db_name):
    """get states"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:

            result = session.query(City, State).join(
                    State, City.state_id == State.id).all()

            if result:

                for city, state in result:
                    print(f"{city.id}: {city.name} -> {state.name}")

        except SQLAlchemyError as e:
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

        get_state_with_city(user, pw, db_name)
