#!/usr/bin/python3
'''Script lists all states from the database hbtn_0e_0_usa '''

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
