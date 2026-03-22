#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşuluruq
    # sys.argv[1]: username, sys.argv[2]: password, sys.argv[3]: database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Kursor yaradırıq ki, SQL əmrlərini icra edək
    cursor = db.cursor()
    
    # Şəkildəki tələbə uyğun SQL sorğusu
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Bütün sətirləri alırıq
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Kursoru və bazanı bağlayırıq
    cursor.close()
    db.close()
