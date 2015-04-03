# coding=utf-8
import conn_db


def compute_balance(acct_number):
    balance = 0
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT Amount FROM Transactions WHERE Acct_Number = '{0}'""".format(acct_number)
    c.execute(query)
    data = c.fetchall()
    for row in data:
        balance += row[0]
    conn_db.close_connection(conn)
    return balance


def valid_account(acct_number):
    present = 0
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Accounts WHERE Acct_Number = '{0}') AS Does_Exist""".format(acct_number)
    c.execute(query)
    for (Does_Exist) in c:
        present = Does_Exist
    conn_db.close_connection(conn)
    present = int(''.join(map(str, present)))
    return present