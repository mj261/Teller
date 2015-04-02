#coding=utf-8
__author__ = 'Matthew Jones', 'Daniel Downs', 'Jennifer Jozefiak', 'Grant Richards', 'Ian Turnipseed'

import SelectionScreens
import sys

selection = SelectionScreens.home_screen()
if selection == 1:
    SelectionScreens.user()
elif selection == 2:
    SelectionScreens.bank_teller()
elif selection == 3:
    SelectionScreens.system_admin()
elif selection == "quit" or selection == "exit":
    sys.exit(0)