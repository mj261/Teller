# coding=utf-8
"""User, Admin, & Teller logins"""
import conn_db
import random
from passlib.hash import pbkdf2_sha256


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


def encrypt_password(clear_password):
    """Password Encryption"""
    encrypted_password = pbkdf2_sha256.encrypt(clear_password, rounds=200000, salt_size=16)
    return encrypted_password


def user_login(username, password):
    """User Login"""
    user_name = ''
    password_hash = ''
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Password FROM Users WHERE Username = '{0}' LIMIT 1""".format(username)
    cursor.execute(query)
    for database_password in cursor:
        password_hash = ''.join(map(str, database_password))
    try:
        login = pbkdf2_sha256.verify(password, password_hash)
    except ValueError:
        login = False
    if not login:
        cursor.close()
        conn_db.close_connection(conn)
        user_name = ''
        return user_name
    else:
        conn = conn_db.connect()
        cursor = conn.cursor()
        query = """SELECT Name FROM Users WHERE Username = '{0}' LIMIT 1""".format(username)
        cursor.execute(query)
        for user_name in cursor:
            user_name = ''.join(map(str, user_name))
        cursor.close()
        conn_db.close_connection(conn)
        return user_name


def admin_login(username, password):
    admin_name = ''
    password_hash = ''
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT Password FROM Admins WHERE Username = '{0}' LIMIT 1""".format(username)
    cursor.execute(query)
    for database_password in cursor:
        password_hash = ''.join(map(str, database_password))
    try:
        login = pbkdf2_sha256.verify(password, password_hash)
    except ValueError:
        login = False
    if not login:
        cursor.close()
        conn_db.close_connection(conn)
        admin_name = ''
        return admin_name
    else:
        conn = conn_db.connect()
        cursor = conn.cursor()
        query = """SELECT Name FROM Admins WHERE Username = '{0}' LIMIT 1""".format(username)
        cursor.execute(query)
        for admin_name in cursor:
            admin_name = ''.join(map(str, admin_name))
        cursor.close()
        conn_db.close_connection(conn)
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


def check_admin_username(username):
    """Check if admin username exists"""
    present = 0
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Admins WHERE Username = '{0}') AS Does_Exist"""\
        .format(username)
    cursor.execute(query)
    for does_exist in cursor:
        present = does_exist
    conn_db.close_connection(conn)
    present = int(''.join(map(str, present)))
    return present


def create_new_teller(teller_name, admin_username):
    """Create new teller"""
    teller_number = 0
    present = 1
    while present == 1:
        rng = random.SystemRandom()
        teller_number = rng.randint(1000000000, 9999999999)
        conn = conn_db.connect()
        cursor = conn.cursor()
        query = """SELECT EXISTS(SELECT * FROM Tellers WHERE Code = '{0}') AS Does_Exist"""\
            .format(teller_number)
        cursor.execute(query)
        for does_exist in cursor:
            present = does_exist
        conn_db.close_connection(conn)
        present = int(''.join(map(str, present)))
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """INSERT INTO Tellers VALUES ('{0}', '{1}')"""\
        .format(teller_name, teller_number)
    cursor.execute(query)
    cursor.close()
    operation = "Create new teller {0} with login code {1}".format(teller_name, teller_number)
    cursor = conn.cursor()
    query = """INSERT INTO Admin_Log (User, Operation) VALUES ('{0}', '{1}')"""\
        .format(admin_username, operation)
    cursor.execute(query)
    cursor.close()
    return teller_number


def create_new_admin(admin_username, new_admin_username, admin_name, admin_email, admin_password):
    """Create new admin"""
    admin_password = encrypt_password(admin_password)
    conn = conn_db.connect()
    cursor = conn.cursor()
    query = """INSERT INTO Admins VALUES ('{0}', '{1}', '{2}', '{3}')"""\
        .format(admin_name, new_admin_username, admin_password, admin_email)
    cursor.execute(query)
    cursor.close()
    operation = "Create new admin {0} with username {1}".format(admin_name, new_admin_username)
    cursor = conn.cursor()
    query = """INSERT INTO Admin_Log (User, Operation) VALUES ('{0}', '{1}')"""\
        .format(admin_username, operation)
    cursor.execute(query)
    cursor.close()
    return 1
