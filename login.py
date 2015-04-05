# coding=utf-8
"""User, Admin, & Teller logins"""
import conn_db


def teller_login(teller_number):
    """Teller Login"""
    teller_name = ''
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Name FROM Tellers WHERE Code = '{0}'""".format(teller_number)
    cursor.execute(query)
    for name in cursor:
        teller_name = name
    conn_db.close_connection(conn)
    teller_name = ''.join(map(str, teller_name))
    return teller_name


def create_user(username, password, email, name):
    """Create a new user"""
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """INSERT INTO Users VALUES ('{0}', '{1}', '{2}', '{3}')"""\
        .format(name, username, password, email)
    cursor.execute(query)
    return 1


def user_login(username, password):
    """User Login"""
    print "User Logged in"


def admin_login(username, password):
    admin_name = ''
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Name FROM Admins WHERE Username = '{0}' and Password = '{1}'""".format(username, password)
    cursor.execute(query)
    for name in cursor:
        admin_name = name
    conn_db.close_connection(conn)
    admin_name = ''.join(map(str, admin_name))
    return admin_name


def check_email(email):
    """Check if email exists"""
    present = 0
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Users WHERE Email = '{0}') AS Does_Exist""".format(email)
    cursor.execute(query)
    for does_exist in cursor:
        present = does_exist
    conn_db.close_connection(conn)
    present = int(''.join(map(str, present)))
    return present


def check_username(username):
    """Check if username exists"""
    present = 0
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Users WHERE Username = '{0}') AS Does_Exist"""\
        .format(username)
    cursor.execute(query)
    for does_exist in cursor:
        present = does_exist
    conn_db.close_connection(conn)
    present = int(''.join(map(str, present)))
    return present
