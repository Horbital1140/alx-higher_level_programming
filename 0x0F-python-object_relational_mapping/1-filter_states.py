#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = connection.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id"""
    cursor.execute(query)


    row =cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()


    cursor.close()

    connection.close()


