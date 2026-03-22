#!/usr/bin/python3
""" Lists all states from the database hbtn_0d_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Terminaldan gələn arqumentləri alırıq (username, password, database)
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    cur = db.cursor()
    # SQL sorğusunu icra edirik
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Bütün nəticələri gətiririk
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Bağlantıları bağlayırıq
    cur.close()
    db.close()
