#!/usr/bin/python3
'''script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument'''

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost', charset='utf8', port=3360,
                         user=args[1], passwd=args[2], db=args[3])
    cursor = db.cursor()
    # name_sech = MySQLdb.converters.Thing2Literal(args[4], d)
    sql = f"SELECT id, name FROM states WHERE name = '{args[4]}'\
             ORDER BY id ASC"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
