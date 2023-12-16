#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state,
"""

import MySQLdb
from sys import argv


def getData_from_mysql(user, pw, db_name, state_name):
    """function to get data from mysql"""

    host = "localhost"

    query = "SELECT cities.name FROM cities "
    query += "JOIN states ON cities.state_id = states.id AND states.name = %s"
    query += "ORDER BY cities.id;"
    param = (state_name,)

    try:

        db = MySQLdb.connect(host, port=3306,
                             user=user, password=pw, db=db_name)
        cursor = db.cursor()

        try:

            cursor.execute(query, param)
            result = cursor.fetchall()

            print(", ".join(row[0] for row in result))

        except Exception as e:
            print(e)
            return

        cursor.close()
        db.close()
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":

    if len(argv) >= 5:
        getData_from_mysql(argv[1], argv[2], argv[3], argv[4])
