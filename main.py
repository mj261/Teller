__author__ = 'Matthew Jones', 'Daniel Downs', 'Jennifer Jozefiak', 'Grant Richards', 'Ian Turnipseed'

import conn_db

##conn = conn_db.connect()

print("#####################################################")
print("###                                               ###")
print("###              Welcome to our Bank              ###")
print("###                                               ###")
print("###             Downs, Jones, Jozefiak            ###")
print("###             Richards, & Turnipseed            ###")
print("###                                               ###")
print("#####################################################")

selection = 0
while (selection != 1 and selection != 2 and selection != 3):
    print("Please select from the following options:\n\n")
    print("1. User")
    print("2. Bank Teller")
    print("3. System Administrator\n\n")
    selection = input("Please enter your selection:  ")
    if (selection != 1 and selection != 2 and selection != 3):
        print("\n\n#####################################################")
        print("###                                               ###")
        print("###         YOU ENTERED AN INVALID OPTION!        ###")
        print("###                                               ###")
        print("#####################################################\n\n")

print 'You selected %s' % selection

##conn_db.close_connection(conn)