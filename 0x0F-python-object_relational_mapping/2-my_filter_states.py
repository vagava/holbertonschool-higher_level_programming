#!/usr/bin/python3
'''script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument'''

import sys
import MySQLdb

if __name__ == '__main__':
    # get arguments
    args = sys.argv
    # connect to Data Base
    db = MySQLdb.connect(host='localhost', charset='utf8', port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cursor = db.cursor()
    # Describe query
    sql = "SELECT id, name FROM states WHERE name = '{}'\
             ORDER BY id ASC".format(args[4])

    # execute the query
    cursor.execute(sql)
    data = cursor.fetchall()
    # show data
    for row in data:
        if row[1] == args[4]:
            print(row)
    db.close()
