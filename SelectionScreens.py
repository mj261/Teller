# coding=utf-8
import login
import base64
import math
import transactions


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
    teller_name = ''
    teller_number = ''
    while teller_name == '':
        teller_number = raw_input("Please enter your teller number:  ")
        teller_name = login.teller_login(teller_number)
    if teller_name != '':
        teller_home(teller_name, teller_number)


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


def teller_home(teller_name, teller_number):
    before_name = math.ceil((40-len(teller_name))/2)
    after_name = math.floor((39-len(teller_name))/2)
    before = ''
    after = ''
    while before_name > 0:
        before += ' '
        before_name -= 1
    while after_name > 0:
        after += ' '
        after_name -= 1

    print("\n\n#####################################################")
    print("###                                               ###")
    print("###{0}Welcome {1}{2}###".format(before, teller_name, after))
    print("###                                               ###")
    print("#####################################################\n\n")

    selection = 0
    while selection != 1 and selection != 2 and selection != 3 and selection != 4:
        print("Please select from the following options:\n\n")
        print("1. View Account")
        print("2. Withdrawal")
        print("3. Deposit")
        print("4. Transfer\n\n")
        selection = int(raw_input("Please enter your selection:  ").strip())
        if selection != 1 and selection != 2 and selection != 3 and selection !=4:
            print("\n\n#####################################################")
            print("###                                               ###")
            print("###         YOU ENTERED AN INVALID OPTION!        ###")
            print("###                                               ###")
            print("#####################################################\n\n")
        else:
            if selection == 1:
                view_funds_screen(teller_name, teller_number)
            elif selection == 2:
                withdrawal_screen(teller_name, teller_number)
            elif selection == 3:
                deposit_screen(teller_name, teller_number)
            elif selection == 4:
                transfer_screen(teller_name, teller_number)


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


def view_funds_screen(teller_name, teller_number):
    print("\n\n#####################################################")
    print("###                                               ###")
    print("###                 View Account                  ###")
    print("###                                               ###")
    print("#####################################################\n\n")
    acct_exists = 1
    acct_number = int(raw_input("Please enter an account number:  ").strip())
    acct_exists = transactions.valid_account(acct_number)
    while acct_exists == 0:
        print("That is not a valid account number!")
        acct_number = int(raw_input("Please enter an account number:  ").strip())
        acct_exists = transactions.valid_account(acct_number)
    balance = transactions.compute_balance(acct_number)
    print("Account Number: {0} has a balance of ${1:.2f}".format(acct_number, balance))
    go_home = raw_input("Press <enter> to continue")
    if 'go_home' in locals():
        teller_home(teller_name, teller_number)
    else:
        print "error"


def withdrawal_screen(teller_name, teller_number):
    print("\n\n#####################################################")
    print("###                                               ###")
    print("###                Withdraw Funds                 ###")
    print("###                                               ###")
    print("#####################################################\n\n")


def deposit_screen(teller_name, teller_number):
    print("\n\n#####################################################")
    print("###                                               ###")
    print("###                 Deposit Funds                 ###")
    print("###                                               ###")
    print("#####################################################\n\n")


def transfer_screen(teller_name, teller_number):
    print("\n\n#####################################################")
    print("###                                               ###")
    print("###                Transfer Funds                 ###")
    print("###                                               ###")
    print("#####################################################\n\n")