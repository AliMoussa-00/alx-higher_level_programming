#!/usr/bin/python3
"""
a script that lists all State objects from the database 'hbtn_0e_6_usa'

    - Your script should take 3 arguments: 'mysql username',
    'mysql password' and 'database name'
    - You must use the module 'SQLAlchemy'
    - You must import 'State' and 'Base' from 'model_state' -
            "from model_state import Base, State"
    - Your script should connect to a MySQL server running on
        'localhost' at port '3306'
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

        states = session.query(State).all()

        for state in states:
            print(f"{state.id}: {state.name}")

        session.close()
