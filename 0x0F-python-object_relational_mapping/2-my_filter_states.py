#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = connection.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    row = curs.fetchone()
    while row is None:
        print(row)
        row = curs.fetchone()

        curs.close()

        connection.close()

