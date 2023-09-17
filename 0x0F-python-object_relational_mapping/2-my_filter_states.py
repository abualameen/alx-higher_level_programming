#!/usr/bin/python3
"""
this module takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

"""


import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name> <name_of_state>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    name_of_state = sys.argv[4].split(',')

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
        )
        cursor = db.cursor()
        query = """
            SELECT * FROM states
            WHERE name IN ({})
            ORDER BY id ASC
            """.format(', '.join(['%s'] * len(name_of_state)))
        cursor.execute(query, name_of_state)
        results = cursor.fetchall()
        if not results:
            print("No states found for '{}'".format(name_of_state))
        else:
            for row in results:
                print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
