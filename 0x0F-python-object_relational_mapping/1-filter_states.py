#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    host = "localhost"

    sql_query = "SELECT id, name FROM states WHERE name like 'N%' ORDER BY id;"

    db = MySQLdb.connect(
            host=host, port=3306, user=argv[1], password=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute(sql_query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
