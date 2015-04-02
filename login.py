# coding=utf-8
import conn_db


def teller_login(teller_number):
    teller_login_status = 0
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Tellers WHERE Code = '{0}') AS Does_Exist""".format(teller_number)
    c.execute(query)
    for (Does_Exist) in c:
        teller_login_status = Does_Exist
    conn_db.close_connection(conn)
    teller_login_status = int(''.join(map(str, teller_login_status)))
    return teller_login_status


def create_user(username, password, email, name):
    conn = conn_db.connect()
    c = conn.cursor()
    query = """INSERT INTO Users VALUES ('{0}', '{1}', '{2}', '{3}')""".format(name, username, password, email)
    c.execute(query)
    return 1


def user_login(username, password):
    print "User Logged in"


def check_email(email):
    present = 0
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Users WHERE Email = '{0}') AS Does_Exist""".format(email)
    c.execute(query)
    for (Does_Exist) in c:
        present = Does_Exist
    conn_db.close_connection(conn)
    present = int(''.join(map(str, present)))
    return present


def check_username(username):
    present = 0
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Users WHERE Username = '{0}') AS Does_Exist""".format(username)
    c.execute(query)
    for (Does_Exist) in c:
        present = Does_Exist
    conn_db.close_connection(conn)
    present = int(''.join(map(str, present)))
    return present
