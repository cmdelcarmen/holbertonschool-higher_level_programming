#!/usr/bin/python3
''' Write a script that lists all states with a name starting with N(upper N)
from the databse hbtn_0e_0_usa '''

import sys
import MySQLdb

if __name__ == "__main__":

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    ''' Open the connection to the databse '''
    database = MySQLdb.connect(host, user, password, database)

    cursor = database.cursor()

    sql_query = "SELECT * FROM states WHERE name REGEXP '^[n]'\
            ORDER BY states.id ASC"

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        database.rollback

    database.close()
