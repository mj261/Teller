# coding=utf-8
"""Database Connection"""
import mysql.connector
from mysql.connector import Error
from mysql.connector.constants import ClientFlag
import SelectionScreens


def connect():
    """Connect to Database"""
    try:
        config = {
            'user': 'SecureTeller',
            'password': 'B@nkT311er',
            'host': 'ec2-52-4-116-111.compute-1.amazonaws.com',
            'database': 'BankTeller',
            'client_flags': [ClientFlag.SSL],
            'ssl_ca': '',
            'ssl_cert': 'client-cert.pem',
            'ssl_key': 'client-key.pem',
        }
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
        else:
            print "No Database Connection"
            SelectionScreens.home_screen()
    except Error as error:
        print "No Database Connection"
        print "ERROR: {0}".format(error)
        SelectionScreens.home_screen()


def close_connection(conn):
    """Close Database Connection"""
    conn.close()
