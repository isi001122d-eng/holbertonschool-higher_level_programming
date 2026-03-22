#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Terminal arqumentlərindən məlumatları alırıq
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    # SQL sorğusu: Adı 'N' ilə başlayanları seç və id-yə görə sırala
    # 'N%' ifadəsi N ilə başlayan hər şeyi bildirir
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    # Nəticələri əldə edirik
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Kursor və bağlantını bağlayırıq
    cursor.close()
    db.close()
