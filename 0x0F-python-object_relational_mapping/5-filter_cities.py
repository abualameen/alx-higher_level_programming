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
    city_names = []
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )
    cursor = db.cursor()
    query = "SELECT cities.name " \
            "FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE states.name = %s " \
            "ORDER BY cities.id ASC "
    cursor.execute(query, (name_of_state,))
    results = cursor.fetchall()
    city_names = [r[0] for r in results]
    if city_names:
        print(f"{', '.join(city_names)}")
    else:
        print(f"No cities found for {state_name}")
    cursor.close()
    db.close()
