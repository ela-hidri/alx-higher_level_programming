#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the database
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    if len(argv) == 4:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            if (row[1][0] == 'N'):
                print(row)
        cur.close()
        db.close()
