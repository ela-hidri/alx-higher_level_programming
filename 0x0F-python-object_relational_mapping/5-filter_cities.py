#!/usr/bin/python3
"""
lists all cities of a state
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    if len(argv) >= 4:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities" +
                    " INNER JOIN states on cities.state_id = states.id" +
                    " where states.name = %(name)s order by cities.id",
                    {'name': argv[4]})
        rows = cur.fetchall()
        print(", ".join([row[0] for row in rows]))
        cur.close()
        db.close()
