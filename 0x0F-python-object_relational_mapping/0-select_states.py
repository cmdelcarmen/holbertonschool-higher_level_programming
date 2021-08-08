#!/usr/bin/python3


import sys
import MySQLdb

if __name__ == "__main__":

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    ''' Open the connection to the databse '''
    database = MySQLdb.connect(host, user, password, database)

    print(type(database))
    print(database)

    cursor = database.cursor()

    ''' SQL squery '''
    sql_query = "SELECT * FROM states ORDER BY states.id ASC"

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        database.rollback

    database.close()
