#!/usr/bin/python3
'''script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa'''
import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, charset='utf8',
                         user=args[1], passwd=args[2], db=args[3])
    cursor = db.cursor()
    sql = '''SELECT id, name FROM states
            WHERE name LIKE 'N%'
            ORDER BY id ASC;'''
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
