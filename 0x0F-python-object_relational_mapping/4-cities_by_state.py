#!/usr/bin/python3
"""
displays matching name
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    if len(argv) >= 4:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities" +
                    " INNER JOIN states on cities.state_id = states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
