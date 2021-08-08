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
    state = sys.argv[4]

    ''' Open the connection to the databse '''
    database = MySQLdb.connect(host, user, password, database)

    cursor = database.cursor()

    sql_query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(state)

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
                print(row)
    except:
        database.rollback

    database.close()
