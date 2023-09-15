#!/usr/bin/python3
'''Write a script that lists all states with a name starting with N'''
import sys
import MySQLdb


if __name__ == "__main__":
    name = sys.argv[1]
    data = sys.argv[3]
    db = MySQLdb.connect(user=name, passwd=sys.argv[2], db=data)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
