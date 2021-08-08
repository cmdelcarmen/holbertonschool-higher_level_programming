#!/usr/bin/python3
''' Write a script that takes an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument '''

import sys
import MySQLdb

if __name__ == "__main__":

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4].split(' ')
    state = state[0]

    ''' Open the connection to the databse '''
    database = MySQLdb.connect(host, user, password, database)

    cursor = database.cursor()

    sql_query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY '{}'\
            ORDER BY cities.id ASC".format(state)

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cities = ""
        for row in results:
            cities += row[1]
            cities += ", "
        print(cities[:-2])
    except:
        database.rollback

    database.close()
