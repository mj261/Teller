#coding=utf-8
__author__ = 'Matthew Jones', 'Daniel Downs', 'Jennifer Jozefiak', 'Grant Richards', 'Ian Turnipseed'

import conn_db
import SelectionScreens

##conn = conn_db.connect()

selection = SelectionScreens.home_screen()
if selection == 1:
    SelectionScreens.user()
elif selection == 2:
    SelectionScreens.bank_teller()
elif selection == 3:
    SelectionScreens.system_admin()

##conn_db.close_connection(conn)