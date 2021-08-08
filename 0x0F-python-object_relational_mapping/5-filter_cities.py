#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":

    data_base, password, user = sys.argv[3], sys.argv[2], sys.argv[1]
    name_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, db=data_base,
                         user=user)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.name
                    FROM states
                    INNER JOIN cities
                    ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC""", (name_state,))

    select_cities = cursor.fetchall()

    city = []
    for data in select_cities:
        city.append(data[0])

    print(*city, sep=", ")

    cursor.close()
    db.close()
