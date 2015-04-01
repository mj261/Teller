# coding=utf-8


def home_screen():
    print("#####################################################")
    print("###                                               ###")
    print("###              Welcome to our Bank              ###")
    print("###                                               ###")
    print("###             Downs, Jones, Jozefiak            ###")
    print("###             Richards, & Turnipseed            ###")
    print("###                                               ###")
    print("#####################################################")

    selection = 0
    while selection != 1 and selection != 2 and selection != 3:
        print("Please select from the following options:\n\n")
        print("1. User")
        print("2. Bank Teller")
        print("3. System Administrator\n\n")
        selection = input("Please enter your selection:  ")
        if selection != 1 and selection != 2 and selection != 3:
            print("\n\n#####################################################")
            print("###                                               ###")
            print("###         YOU ENTERED AN INVALID OPTION!        ###")
            print("###                                               ###")
            print("#####################################################\n\n")

    return selection


def bank_teller():
    print "Bank Teller Screen"


def system_admin():
    print "Admin"


def user():
    print "User"