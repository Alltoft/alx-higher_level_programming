#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys

if __name__ == "__main__":
    Mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )
    cur = Mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    Mydb.close()
