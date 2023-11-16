#!/usr/bin/python3
"""
this module takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

"""
import sys
import mysql.connector

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name> <name_of_state>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    name_of_state = sys.argv[4]
    
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )
    
    cursor = db.cursor()
    
    # Unsafe code: String concatenation without proper escaping
    query = "SELECT * FROM states WHERE name = '" + name_of_state + "' ORDER BY id ASC"
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    cursor.close()
    db.close()

