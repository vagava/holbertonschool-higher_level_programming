#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''
import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    # connect to Data Base
    db = MySQLdb.connect(host='localhost', port=3360,
                         user=args[1], passwd=args[2], db=args[3])
    # Describe the query
    sql = '''
            SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
        '''
    # execute query
    with db.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
    # display data
    for row in data:
        print(row)
    # close Data Base
    db.close()
