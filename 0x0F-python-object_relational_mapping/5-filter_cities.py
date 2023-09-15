#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    name = argv[1]
    data = argv[3]
    search = argv[4]
    db = MySQLdb.connect(user=name, passwd=argv[2], db=data)
    cur = db.cursor()
    query = "SELECT c.name \
        FROM cities AS c \
            JOIN states AS s \
                ON s.id = c.state_id \
                    where s.name = %s"
    cur.execute(query, (search,))
    rows = cur.fetchall()
    city = ()
    for row in rows:
        city += row
    print(*city, sep=", ")
    cur.close()
    db.close()
