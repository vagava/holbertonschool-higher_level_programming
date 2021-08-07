#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    bd = MySQLdb.connect(host="localhost", user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cursor = bd.cursor()
    sql = "SELECT id, name FROM states; ORDER BY id ASC"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    bd.close()
