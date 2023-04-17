#!/usr/bin/python3
"""
Method of use: 
./0-select_states.py <mysql username> <mysql password> <database name>

"""
import sys 
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306, host='localhost')
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    rows = c.fetchall()
    for row in rows:
        print(row)
