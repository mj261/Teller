# coding=utf-8
import conn_db
import time


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


def account_owner(acct_number):
    name = ''
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT Name FROM Users WHERE Username=(SELECT User FROM Accounts WHERE Acct_Number = '{0}' LIMIT 1) \
    LIMIT 1""".format(acct_number)
    c.execute(query)
    data = c.fetchall()
    for row in data:
        name = row[0]
    conn_db.close_connection(conn)
    return name


def get_username(acct_number):
    username = ''
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT User FROM Accounts WHERE Acct_Number = '{0}' LIMIT 1""".format(acct_number)
    c.execute(query)
    data = c.fetchall()
    for row in data:
        username = row[0]
    conn_db.close_connection(conn)
    return username


def alternate_accounts(username, acct_number):
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT Acct_Number, Type FROM Accounts WHERE User = '{0}' AND Acct_Number != {1} LIMIT 1"""\
        .format(username, acct_number)
    c.execute(query)
    data = c.fetchall()
    conn_db.close_connection(conn)
    return data


def withdraw(acct_number, amount):
    epoch = time.time()
    conn = conn_db.connect()
    c = conn.cursor()
    query = """INSERT INTO `Transactions`(`Acct_Number`, `Amount`, `Time`) VALUES ({0},{1},{2})"""\
        .format(acct_number, amount, epoch)
    c.execute(query)
    conn_db.close_connection(conn)


def verify_funds(acct_number, amount):
    balance = compute_balance(acct_number)
    if amount <= balance:
        return 1
    else:
        return 0