#!/usr/bin/python3
"""
a script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sys import argv
from relationship_state import Base, State
from relationship_city import City


def get_state_with_city(user, pw, db_name):
    """get states with their cities"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Base.metadata.create_all(eng)
        Session = sessionmaker(bind=engine)
        session = Session()

        try:

            res = session.query(State).outerjoin(City).all()

            if res:

                for state in res:
                    print(f"{state.id}: {state.name}")

                    for city in state.cities:
                        print(f"    {city.id}: {city.name}")

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
