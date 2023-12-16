#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def getData_from_mysql(user, pw, db_name):
    """function to get data from mysql"""

    host = "localhost"

    query = "SELECT cities.id, cities.name, states.name FROM cities "
    query += "JOIN states ON cities.state_id = states.id ORDER BY cities.id;"

    try:

        db = MySQLdb.connect(host, port=3306,
                             user=user, password=pw, db=db_name)
        cursor = db.cursor()

        try:

            cursor.execute(query)
            result = cursor.fetchall()

            for row in result:
                print(row)

        except Exception as e:
            print(e)
            return

        cursor.close()
        db.close()
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":

    if len(argv) >= 4:
        getData_from_mysql(argv[1], argv[2], argv[3])
