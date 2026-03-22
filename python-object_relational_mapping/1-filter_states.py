#!/usr/bin/python3
""" Lists all states starting with N from the database """
import MySQLdb
import sys

if __name__ == "__main__":
    # Bağlantı qururuq (localhost port 3306)
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], 
                         db=sys.argv[3])
    
    cursor = db.cursor()
    # 'N%' N ilə başlayan deməkdir, BINARY isə böyük-kiçik hərfi ayırd edir
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
