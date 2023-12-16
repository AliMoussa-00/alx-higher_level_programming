#!/usr/bin/python3
"""
 a script that lists all states from the database hbtn_0e_0_usa:
 Thescript should take 3 arguments:
    mysql username, mysql password and database name (no validation needed)
"""

import MySQLdb
from sys import argv


def getData_from_mysql(user, pw, database):
    """Implementing getting data from MySQL DB"""

    sql_query = "SELECT id, name FROM states ORDER BY id"

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, password=pw, db=database)

    cursor = db.cursor()

    try:
        cursor.execute(sql_query)

        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        db.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":

    if (len(argv) >= 4):

        getData_from_mysql(argv[1], argv[2], argv[3])
