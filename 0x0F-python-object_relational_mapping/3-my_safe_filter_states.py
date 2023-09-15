#!/usr/bin/python3
"""Write a script that takes in an argument"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    name = argv[1]
    data = argv[3]
    search = argv[4]
    db = MySQLdb.connect(user=name, passwd=argv[2], db=data)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (search,))
    [print(row) for row in cur.fetchall()]
    cur.close()
    db.close()
