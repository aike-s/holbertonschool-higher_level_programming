#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]

    db = MySQLdb.connect(host="localhost", port=3306, db=data_base,
                         user=user)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id ASC""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
