#!/usr/bin/python3
"""Filter states by user input"""


import MySQLdb
from sys import argv

if "__main__" == __name__:
    data = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])

    cur = data.cursor()

    # Execute the query
    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    finaldata = cur.fetchall()

    for dt in finaldata:
        print(dt)

    cur.close()
    data.close()
