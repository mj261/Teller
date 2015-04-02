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
        teller_home()


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
    user_selection = ''
    while user_selection != 'y' and user_selection != 'n':
        print("Are you a new user?")
        user_selection = raw_input("(Y)es or (N)o? ").strip().lower()
        if user_selection == 'y':
            new_user()
        elif user_selection == 'n':
            old_user()


def new_user():
    print("Welcome New User!")
    username = ''
    email = ''
    email_check = 1
    username_check = 1
    name = raw_input("Please enter your name: ")
    while email_check != 0:
        email = raw_input("Please enter your email address: ")
        email_check = login.check_email(email)
        if email_check == 1:
            print "Email Address is in use. You already have an account!"
    while username_check != 0:
        username = raw_input("Please select your username: ")
        username_check = login.check_username(username)
        if username_check == 1:
            print "Username is in use.  Please select another!"
    password = raw_input("Please select your password: ")

    password = password_check(password)
    success = login.create_user(username, password, email, name)
    if success == 1:
        user_home()
    else:
        print("There was an error! Please try again.")
        home_screen()


def old_user():
    user_username = raw_input("Please enter your username:  ")
    user_password = raw_input("Please enter your password:  ")


def teller_home():
    print "Teller Home Screen"


def user_home():
    print "User Home Screen"


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
        return encode