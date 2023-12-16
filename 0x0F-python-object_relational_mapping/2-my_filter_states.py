#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argumen
"""

import MySQLdb
from sys import argv


def getData_from_mysql(user, pw, database, name_param):
    """Function to get data from MySQL DB"""

    host = "localhost"

    sql_query = "SELECT id, name FROM states "
    sql_query += "WHERE name LIKE BINARY '{}' ORDER BY id;".format(name_param)

    db = MySQLdb.connect(host=host, port=3306,
                         user=user, password=pw, db=database)

    cursor = db.cursor()

    try:
        cursor.execute(sql_query)

        results = cursor.fetchall()

        for row in results:
            print(row)

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":

    if len(argv) >= 5:

        getData_from_mysql(argv[1], argv[2], argv[3], argv[4])
