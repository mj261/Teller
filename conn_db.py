# coding=utf-8
import mysql.connector
from mysql.connector import Error


def connect():
    try:
        conn = mysql.connector.connect(user='Teller', password='B@nkT311er',
                                       host='ec2-52-4-116-111.compute-1.amazonaws.com',
                                       database='BankTeller')
        if conn.is_connected():
            return conn

    except Error as e:
        print(e)


def close_connection(conn):
    conn.close()
    # if not conn.is_connected():
    #     print ("Connection Closed")