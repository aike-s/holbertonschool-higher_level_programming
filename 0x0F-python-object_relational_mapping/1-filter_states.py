#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""

import MySQLdb
import sys

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]

    db = MySQLdb.connect(host="localhost", port=3306, db=data_base,
                         passwd=password, user=user)

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
                    WHERE `name` LIKE 'N%'
                    ORDER BY states.id ASC""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
