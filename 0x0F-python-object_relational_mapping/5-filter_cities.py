#!/usr/bin/python3
''' script that takes in the name of a state as an
argument and lists all cities of that state, using
the database hbtn_0e_4_usa '''

import sys
import MySQLdb

if __name__ == '__main__':
    # get arguments
    program, username, passwd, db, state_name = sys.argv
    # connect to Data Base
    db = MySQLdb.connect(host='localhost', port=3360, charset='utf8',
                         user=username, passwd=passwd, db=db)
    # describe the query
    sql = """
            SELECT cities.name FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            WHERE states.name = '%s'
            ORDER BY cities.id ASC;
        """
    # execute query
    with db.cursor() as cursor:
        cursor.execute(sql, (state_name,))
        data = cursor.fetchall()
    # Show Data
    for i in range(len(data)):
        if i != len(data)-1:
            print(data[i][0], end=", ")
        else:
            print(data[i][0])
    # close Data base
    db.close()
