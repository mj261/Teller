__author__ = 'Matthew Jones', 'Daniel Downs', 'Jennifer Jozefiak', 'Grant Richards', 'Ian Turnipseed'

import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(user='Teller', password='B@nkT311er',
                              host='ec2-52-4-116-111.compute-1.amazonaws.com',
                              database='BankTeller')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

connect()