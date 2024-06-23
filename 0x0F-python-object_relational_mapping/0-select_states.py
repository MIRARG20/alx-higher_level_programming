#!/usr/bin/python3
"""
this script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(
        host = "localhost", user=argv[1], port=3306, pasword=argv[2], database=argv[3])

    # creat a curcor
    cr = db.cursor()

    # Execute the query
    cr.excute("select * from states")

    # fetch all rows

    rows = cr.fetchall()

    for row in rows:
        print(row)
