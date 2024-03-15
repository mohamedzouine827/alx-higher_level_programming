#!/usr/bin/python3
"""Filter states by user input"""


import MySQLdb
from sys import argv

if "__main__" == __name__:
    # Establish connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    # Create a cursor object
    cur = db.cursor()

    s = argv[4]

    # Execute the SQL query
    query = ("SELECT * FROM states WHERE name LIKE '{}%' "
             "ORDER BY id ASC".format(s))
    cur.execute(query, (s,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
