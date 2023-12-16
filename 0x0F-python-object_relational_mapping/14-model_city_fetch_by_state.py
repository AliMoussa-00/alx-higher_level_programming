#!/usr/bin/python3
"""
 a script 14-model_city_fetch_by_state.py that prints all City objects
 from the database hbtn_0e_14_usa
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sys import argv
from model_state import Base, State
from model_city import City


def getData_from_cities_states(user, pw, db_name):
    """Getting data"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pw, db_name), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:

            cities = session.query(City, State).join(
                    State, City.state_id == State.id).all()

            for city, state in cities:
                print(f"{state.name}: ({city.id}) {city.name}")

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

        getData_from_cities_states(user, pw, db_name)
