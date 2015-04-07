# coding=utf-8
"""Database Transactions"""
import conn_db
import time
import json
import urllib2
from validate_email import validate_email
import getpass
import login


def compute_balance(acct_number):
    """Compute Balance"""
    balance = 0
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Amount FROM Transactions WHERE Acct_Number = '{0}'""".format(acct_number)
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        balance += row[0]
    conn_db.close_connection(conn)
    return balance


def valid_account(acct_number):
    """Check for valid account"""
    present = 0
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Accounts WHERE Acct_Number = '{0}') AS Does_Exist"""\
        .format(acct_number)
    cursor.execute(query)
    for does_exist in cursor:
        present = does_exist
    conn_db.close_connection(conn)
    present = int(''.join(map(str, present)))
    return present


def account_owner(acct_number):
    """Find account owner"""
    name = ''
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Name FROM Users WHERE Username=(SELECT User FROM Accounts \
        WHERE Acct_Number = '{0}' LIMIT 1) LIMIT 1""".format(acct_number)
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        name = row[0]
    conn_db.close_connection(conn)
    return name


def get_username(acct_number):
    """Return username from account number"""
    username = ''
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT User FROM Accounts WHERE Acct_Number = '{0}' LIMIT 1""".format(acct_number)
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        username = row[0]
    conn_db.close_connection(conn)
    return username


def alternate_accounts(username, acct_number):
    """Find alternate accounts"""
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Acct_Number, Type FROM Accounts WHERE User = '{0}' AND \
        Acct_Number != '{1}' LIMIT 1""".format(username, acct_number)
    cursor.execute(query)
    data = cursor.fetchall()
    conn_db.close_connection(conn)
    return data


def withdraw(acct_number, amount):
    """Withdraw from account"""
    epoch = time.time()
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """INSERT INTO `Transactions`(`Acct_Number`, `Amount`, `Time`) VALUES
        ('{0}','{1}','{2}')""".format(acct_number, amount, epoch)
    cursor.execute(query)
    conn_db.close_connection(conn)


def verify_funds(acct_number, amount):
    """Verify funds in account"""
    balance = compute_balance(acct_number)
    if amount <= balance:
        return 1
    else:
        return 0


def deposit(acct_number, amount):
    """Deposit into account"""
    epoch = time.time()
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """INSERT INTO `Transactions`(`Acct_Number`, `Amount`, `Time`) VALUES
        ('{0}','{1}','{2}')""".format(acct_number, amount, epoch)
    cursor.execute(query)
    conn_db.close_connection(conn)


def currency_converter(currency_from, currency_to, currency_input):
    """Convert Currency"""
    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'\
        + currency_from + currency_to+'")'
    yql_query_url = yql_base_url + "?q=" + yql_query + \
        "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    try:
        yql_response = urllib2.urlopen(yql_query_url)
        try:
            yql_json = json.loads(yql_response.read())
            currency_output = currency_input * float(yql_json['query']['results']['rate']['Rate'])
            return currency_output
        except (ValueError, KeyError, TypeError):
            return "JSON format error"

    except IOError, error:
        if hasattr(error, 'code'):
            return error.code
        elif hasattr(error, 'reason'):
            return error.reason


def get_account_info(acct_number):
    """Find Account Info"""
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Name, Username, Email, Type FROM Accounts LEFT JOIN Users on
        Users.Username = Accounts.User WHERE Acct_Number = '{0}' LIMIT 1""".format(acct_number)
    cursor.execute(query)
    data = cursor.fetchall()
    conn_db.close_connection(conn)
    return data


def modify_account_type(admin_username, acct_number):
    """Change Account Type"""
    new_type = ''
    while new_type != 'C' and new_type != 'S':
        new_type = raw_input("Please enter an account type (C)hecking or (S)avings for account "
                             "{0}:  ".format(acct_number)).upper()
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """UPDATE Accounts SET Type = '{0}' WHERE Acct_Number = '{1}'"""\
        .format(new_type, acct_number)
    cursor.execute(query)
    cursor.close()
    conn_db.close_connection(conn)
    conn = conn_db.connect()
    cursor = conn.cursor()
    operation = "Changed account number {0} to type {1}".format(acct_number, new_type)
    query = """INSERT INTO Admin_Log (User, Operation) VALUES ('{0}', '{1}')"""\
        .format(admin_username, operation)
    cursor.execute(query)
    cursor.close()
    conn_db.close_connection(conn)


def modify_account_owner(admin_username, acct_number):
    """Change account owner"""
    name = raw_input("Please enter the account owner's name:  ")
    while not all(x.isalpha() or x.isspace() for x in name):
        name = raw_input("Please enter a valid name:  ")
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """UPDATE Users SET Name = '{0}' WHERE Username = (SELECT User FROM
        Accounts WHERE Acct_Number = '{1}')""".format(name, acct_number)
    cursor.execute(query)
    conn_db.close_connection(conn)
    conn = conn_db.connect()
    cursor = conn.cursor()
    operation = "Changed owner name to {0} for account number {1}".format(name, acct_number)
    query = """INSERT INTO Admin_Log (User, Operation) VALUES ('{0}', '{1}')"""\
        .format(admin_username, operation)
    cursor.execute(query)
    cursor.close()
    conn_db.close_connection(conn)


def modify_account_email(admin_username, acct_number):
    """Change account email"""
    email = raw_input("Please enter the account owner's email:  ")
    while not validate_email(email):
        email = raw_input("Please enter a valid email:  ")
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """UPDATE Users SET Email = '{0}' WHERE Username = (SELECT User FROM Accounts
        WHERE Acct_Number = '{1}')""".format(email, acct_number)
    cursor.execute(query)
    conn_db.close_connection(conn)
    conn = conn_db.connect()
    cursor = conn.cursor()
    operation = "Changed owner email to {0} for account number {1}".format(email, acct_number)
    query = """INSERT INTO Admin_Log (User, Operation) VALUES ('{0}', '{1}')"""\
        .format(admin_username, operation)
    cursor.execute(query)
    cursor.close()
    conn_db.close_connection(conn)


def modify_account_password(admin_username, acct_number):
    """Change account password"""
    password = getpass.getpass("Please enter a password:  ")
    password_verify = getpass.getpass("Please verify your password:  ")
    while password != password_verify:
        print "\n\nYour passwords did not match!\n\n"
        password = getpass.getpass("Please enter a password:  ")
        password_verify = getpass.getpass("Please verify your password:  ")
    password = login.encrypt_password(password)
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """UPDATE Users SET Password = '{0}' WHERE Username = (SELECT User FROM Accounts
        WHERE Acct_Number = '{1}')""".format(password, acct_number)
    cursor.execute(query)
    conn_db.close_connection(conn)
    conn = conn_db.connect()
    cursor = conn.cursor()
    operation = "Changed password for account number {0}".format(acct_number)
    query = """INSERT INTO Admin_Log (User, Operation) VALUES ('{0}', '{1}')"""\
        .format(admin_username, operation)
    cursor.execute(query)
    cursor.close()
    conn_db.close_connection(conn)
