#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
(safe from MySQL injections!)
"""

import MySQLdb
import sys

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]
    argument = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, db=data_base,
                         passwd=password, user=user)

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
                    WHERE states.name=%s
                    ORDER BY states.id""", (argument,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
