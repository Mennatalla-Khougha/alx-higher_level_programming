#!/usr/bin/python3
'''This script lists all states from database hbtn_0e_0_usa'''
import sys
import MySQLdb


if __name__ == "__main__":
    name = sys.argv[1]
    data = sys.argv[3]
    db = MySQLdb.connect(user=name, passwd=sys.argv[2], db=data)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
