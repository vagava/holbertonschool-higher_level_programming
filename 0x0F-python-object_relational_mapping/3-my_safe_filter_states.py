#!/usr/bin/python3
'''script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections'''

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost', charset='utf8', port=3360,
                         user=args[1], passwd=args[2], db=args[3])
    cursor = db.cursor()
    name_search = args[4]
    sql = "SELECT id, name FROM states WHERE name=%s \
            ORDER BY id ASC"
    cursor.execute(sql, (name_search, ))
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
