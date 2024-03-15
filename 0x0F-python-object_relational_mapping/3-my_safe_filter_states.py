#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
from sys import argv

if "__main__" == __name__:
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    s = argv[4]

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, (s + '%',))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
