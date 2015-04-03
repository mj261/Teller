# coding=utf-8
import mysql.connector
from mysql.connector import Error
from mysql.connector.constants import ClientFlag


def connect():
    try:
        config = {
            'user': 'SecureTeller',
            'password': 'B@nkT311er',
            'host': 'ec2-52-4-116-111.compute-1.amazonaws.com',
            'database': 'BankTeller',
            'client_flags': [ClientFlag.SSL],
            'ssl_ca': 'ca.pem',
            'ssl_cert': 'client-cert.pem',
            'ssl_key': 'client-key.pem',
        }
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            #print "Connected"
            return conn

    except Error as e:
        print(e)


def close_connection(conn):
    conn.close()
    # if not conn.is_connected():
    #     print ("Connection Closed")