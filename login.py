# coding=utf-8
import conn_db


def teller_login(teller_number):
    teller_login_status = 0
    conn = conn_db.connect()
    c = conn.cursor()
    query = """SELECT EXISTS(SELECT * FROM Tellers WHERE Code = '%s') AS Does_Exist""" % teller_number
    c.execute(query)
    for (Does_Exist) in c:
        teller_login_status = Does_Exist
    conn_db.close_connection(conn)
    teller_login_status = int(''.join(map(str,teller_login_status)))
    return teller_login_status