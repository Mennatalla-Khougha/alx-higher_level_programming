#!/usr/bin/python3
""" lists all cities"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    name = argv[1]
    data = argv[3]
    db = MySQLdb.connect(user=name, passwd=argv[2], db=data)
    cur = db.cursor()
    query = "SELECT c.id, c.name, s.name \
        FROM cities AS c \
            JOIN states AS s \
                ON s.id = c.state_id"
    cur.execute(query)
    [print(row) for row in cur.fetchall()]
    cur.close()
    db.close()
