#!/usr/bin/python3
"""Filter states by user input"""


import MySQLdb
from sys import argv

if "__main__" == __name__:
    data = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    state_name = argv[4]
    cursor = data.cursor()
    cursor.execute(
        'SELECT cities.name FROM cities' +
        ' INNER JOIN states ON cities.state_id = states.id' +
        ' WHERE CAST(states.name AS BINARY) = %s' +
        ' ORDER BY cities.id ASC;',
        [state_name]
    )
    results = cursor.fetchall()
    print(', '.join(map(lambda x: x[0], results)))
    data.close()
