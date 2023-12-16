#!/usr/bin/python3
"""
 a script that takes in arguments and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.
 But this time, write one that is SAFE from
        MySQL injections!
"""


import MySQLdb
from sys import argv


def getData_from_mysql(user, pw, database, name_param):
    """Fucntion to get data from MySQL DB"""

    host = "localhost"

    # the param is always a 'tuple'
    param = (name_param,)

    sql_query = "SELECT id, name FROM states WHERE name = %s ORDER BY id;"

    try:
        db = MySQLdb.connect(host=host, port=3306,
                             user=user, password=pw, db=database)
        cursor = db.cursor()

        try:

            cursor.execute(sql_query, param)

            results = cursor.fetchall()

            for row in results:
                print(row)

        except Exception as e:
            print(e)
            return

    except Exception as e:
        print(e)
        return

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":

    if len(argv) >= 5:

        getData_from_mysql(argv[1], argv[2], argv[3], argv[4])
