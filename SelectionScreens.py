# coding=utf-8
import login
import base64


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
    while selection != 1 and selection != 2 and selection != 3 and selection != "quit" and selection != "exit":
        print("Please select from the following options:\n\n")
        print("1. User")
        print("2. Bank Teller")
        print("3. System Administrator\n\n")
        selection = raw_input("Please enter your selection:  ").lower()
        if selection != "quit" and selection != "exit":
            selection = int(selection)
        if selection != 1 and selection != 2 and selection != 3 and selection != "quit" and selection != "exit":
            print("\n\n#####################################################")
            print("###                                               ###")
            print("###         YOU ENTERED AN INVALID OPTION!        ###")
            print("###                                               ###")
            print("#####################################################\n\n")

    return selection


def bank_teller():
    print("\n\n#####################################################")
    print("###                                               ###")
    print("###              Welcome Bank Teller              ###")
    print("###                                               ###")
    print("#####################################################\n\n")
    login_status = 0
    while login_status != 1:
        teller_selection = raw_input("Please enter your teller number:  ")
        login_status = login.teller_login(teller_selection)
    if login_status == 1:
        print "Teller Logged in"


def system_admin():
    print("\n\n#####################################################")
    print("###                                               ###")
    print("###              Welcome System Admin             ###")
    print("###                                               ###")
    print("#####################################################\n\n")
    admin_username = raw_input("Please enter your username:  ")
    admin_password = raw_input("Please enter your password:  ")


def user():
    print("\n\n#####################################################")
    print("###                                               ###")
    print("###                 Welcome User                  ###")
    print("###                                               ###")
    print("#####################################################\n\n")
    print("Are you a new user?")
    user_selection = raw_input("yes or no? ")
    if user_selection == 'yes':
        new_user()
    elif user_selection == 'no':
        old_user()


def new_user():
    print("Welcome New User!")
    username = raw_input("Please select your username: ")
    password = raw_input("Please select your password: ")
    password_check(password)
    user_username = username
    user_password = password


def old_user():
    user_username = raw_input("Please enter your username:  ")
    user_password = raw_input("Please enter your password:  ")


def password_check(password):
    if len(password) < 6:
        print("Passwords need to be at least 6 long")
        password = raw_input("Please enter again: ")
        password_check(password)
    else:
        # A way to encode/ decode passwords, I just put both in there to look at.
        encode = base64.b64encode(password)
        decode = base64.b64decode(encode)
        print("Password saved")
        print(encode)
        print(decode)