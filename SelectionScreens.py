# coding=utf-8
"""Selection Screen Function"""

import math
import transactions
import sys
import re
import getpass
from validate_email import validate_email
import login


# #TOC
# All roles          Line 
# System Admin       Line
# Teller             Line
# User               Line

##All users
def home_screen():
    """Home Screen presented at Application Startup"""
    print "#####################################################"
    print "###                                               ###"
    print "###              Welcome to our Bank              ###"
    print "###                                               ###"
    print "###             Downs, Jones, Jozefiak            ###"
    print "###             Richards, & Turnipseed            ###"
    print "###                                               ###"
    print "#####################################################"

    selection = 0
    while selection != 1 and selection != 2 and selection != 3 and selection != "quit" \
            and selection != "exit":
        print "Please select from the following options:\n\n"
        print "1. User"
        print "2. Bank Teller"
        print "3. System Administrator\n\n"
        selection = raw_input("Please enter your selection:  ").lower()
        if selection != "quit" and selection != "exit" and selection.isdigit():
            selection = int(selection)
        if selection != 1 and selection != 2 and selection != 3 and selection != "quit" \
                and selection != "exit":
            print "\n\n#####################################################"
            print "###                                               ###"
            print "###         YOU ENTERED AN INVALID OPTION!        ###"
            print "###                                               ###"
            print "#####################################################\n\n"

    if selection == 1:
        user()
    elif selection == 2:
        bank_teller()
    elif selection == 3:
        system_admin()
    elif selection == "quit" or selection == "exit":
        sys.exit(0)


###################################################
##System Admin Functions
def system_admin():
    """System Admin Welcome Screen"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###              Welcome System Admin             ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    admin_username = raw_input("Please enter your username:  ")
    admin_password = getpass.getpass("Please enter your password:  ")
    while admin_username == '' or admin_password == '' or not admin_username.isalnum() \
            or not admin_password.isalnum():
        print "\nYou must enter a valid username and password!\n"
        admin_username = raw_input("Please enter your username:  ")
        admin_password = getpass.getpass("Please enter your password:  ")
    admin_name = login.admin_login(admin_username, admin_password)
    while admin_name == '':
        print "\n\n#####################################################"
        print "###                                               ###"
        print "###                Invalid Login!                 ###"
        print "###                                               ###"
        print "#####################################################\n\n"
        admin_username = raw_input("Please enter your username:  ")
        admin_password = getpass.getpass("Please enter your password:  ")
        while admin_username == '' or admin_password == '' or not admin_username.isalnum() \
                or not admin_password.isalnum():
            print "\nYou must enter a username and password!\n"
            admin_username = raw_input("Please enter your username:  ")
            admin_password = getpass.getpass("Please enter your password:  ")
        admin_name = login.admin_login(admin_username, admin_password)
    admin_home(admin_username, admin_name, 'usd')


def create_admin(admin_username, admin_name, currency):
    """Create Admin by Admin"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                 Create Teller                 ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    username_check = 1
    new_admin_username = ''
    new_admin_name = raw_input("Please enter the System Admin's name:  ")
    while not all(x.isalpha() or x.isspace() for x in new_admin_name):
        new_admin_name = raw_input("Please enter a valid name:  ")
    while username_check != 0:
        new_admin_username = raw_input("Please enter the System Admin's username:  ")
        while not all(x.isalpha() for x in new_admin_username):
            new_admin_username = raw_input("Please enter a valid username:  ")
        username_check = login.check_admin_username(new_admin_username)
        if username_check == 1:
            print "Username is in use.  Please select another!"
    new_admin_email = raw_input("Please enter the System Admin's email:  ")
    while not validate_email(new_admin_email):
        new_admin_email = raw_input("Please enter a valid email:  ")
    new_admin_pass = getpass.getpass("Please enter a password:  ")
    new_admin_pass_verify = getpass.getpass("Please verify your password:  ")
    while new_admin_pass != new_admin_pass_verify:
        print "\n\nYour passwords did not match!\n\n"
        new_admin_pass = getpass.getpass("Please enter a password:  ")
        new_admin_pass_verify = getpass.getpass("Please verify your password:  ")
    success = login.create_new_admin(admin_username, new_admin_username, new_admin_name,
                                     new_admin_email, new_admin_pass)
    if success == 1:
        print "System Administrator has been created for {0} with username: {1}" \
            .format(new_admin_name, new_admin_username)
    else:
        print "User not created."
    raw_input("\nPress <enter> to continue")
    admin_home(admin_username, admin_name, currency)


def admin_home(admin_username, admin_name, currency):
    """Home page for system admin after login"""
    before_name = math.ceil((40 - len(admin_name)) / 2)
    after_name = math.floor((39 - len(admin_name)) / 2)
    before = ''
    after = ''
    while before_name > 0:
        before += ' '
        before_name -= 1
    while after_name > 0:
        after += ' '
        after_name -= 1

    print "\n\n#####################################################"
    print "###                                               ###"
    print "###{0}Welcome {1}{2}###".format(before, admin_name, after)
    print "###                                               ###"
    print "#####################################################\n\n"

    selection = 0
    while selection != 1 and selection != 2 and selection != 3 and selection != 4 \
            and selection != 5 and selection != 6:
        print "Please select from the following options:\n\n"
        print "1. View Account"
        print "2. Modify Account"
        print "3. Create Teller"
        print "4. Create Admin"
        if currency == 'usd':
            print "5. Use Euro Currency"
        else:
            print "5. Use USD Currency"
        print "6. Logout\n\n"
        selection = raw_input("Please enter your selection:  ").strip()
        if selection.isdigit():
            selection = int(selection)
        if selection != 1 and selection != 2 and selection != 3 and selection != 4 \
                and selection != 5 and selection != 6:
            print "\n\n#####################################################"
            print "###                                               ###"
            print "###         YOU ENTERED AN INVALID OPTION!        ###"
            print "###                                               ###"
            print "#####################################################\n\n"
        else:
            if selection == 1:
                view_funds_screen(admin_username, admin_name, currency, 'Admin')
            elif selection == 2:
                admin_modify_account(admin_username, admin_name, currency)
            elif selection == 3:
                create_teller(admin_username, admin_name, currency)
            elif selection == 4:
                create_admin(admin_username, admin_name, currency)
            elif selection == 5:
                if currency == 'usd':
                    currency = 'eur'
                else:
                    currency = 'usd'
                admin_home(admin_username, admin_name, currency)
            elif selection == 6:
                home_screen()


def view_funds_screen(teller_name, teller_number, currency, user_type):
    """View account for tellers and admins"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                 View Account                  ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    acct_number = raw_input("Please enter an account number:  ")
    if acct_number.isdigit():
        acct_exists = transactions.valid_account(acct_number)
    else:
        acct_exists = 0
    while acct_exists == 0:
        print "That is not a valid account number!"
        acct_number = raw_input("Please enter an account number:  ")
        if acct_number.isdigit():
            acct_exists = transactions.valid_account(int(acct_number.strip()))
    name = transactions.account_owner(acct_number)
    username = transactions.get_username(acct_number)
    balance = transactions.compute_balance(acct_number)
    if currency == "eur":
        balance = transactions.currency_converter('usd', 'eur', balance)
    other_accounts = transactions.alternate_accounts(username, acct_number)
    print "\n\nAccount Number: {0}".format(acct_number)
    print "Account Owner: {0}".format(name)
    print "Username: {0}".format(username)
    if currency == "usd":
        print "Account Number {0} has a balance of ${1:.2f}".format(acct_number, balance)
    else:
        balance = float(balance)
        print "Account Number {0} has a balance of €{1:.2f}".format(acct_number, balance)
    print "Alternate Accounts:"
    if other_accounts != '':
        for row in other_accounts:
            balance = transactions.compute_balance(row[0])
            if currency == "eur":
                balance = transactions.currency_converter('usd', 'eur', balance)
                balance = float(balance)
            if row[1] == "C":
                account_type = "Checking"
            else:
                account_type = "Savings"
            if currency == "usd":
                print "\tAccount Number: {0}\tType: {1}\tBalance: ${2:.2f}" \
                    .format(row[0], account_type, balance)
            else:
                print "\tAccount Number: {0}\tType: {1}\tBalance: €{2:.2f}" \
                    .format(row[0], account_type, balance)
    else:
        print "None"
    raw_input("\n\nPress <enter> to continue")
    if user_type == 'Teller':
        teller_home(teller_name, teller_number, currency)
    elif user_type == 'Admin':
        admin_home(teller_name, teller_number, currency)


def admin_modify_account(admin_username, admin_name, currency):
    """Admin modifying account"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                Modify Account                 ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    acct_number = raw_input("Please enter an account number:  ")
    if acct_number.isdigit():
        acct_exists = transactions.valid_account(acct_number)
    else:
        acct_exists = 0
    while acct_exists == 0:
        print "That is not a valid account number!"
        acct_number = raw_input("Please enter an account number:  ")
        if acct_number.isdigit():
            acct_exists = transactions.valid_account(int(acct_number.strip()))
    data = transactions.get_account_info(acct_number)
    username = ''
    acct_type = ''
    name = ''
    email = ''
    for row in data:
        name = row[0]
        username = row[1]
        email = row[2]
        acct_type = row[3]
    balance = transactions.compute_balance(acct_number)
    if currency == "eur":
        balance = transactions.currency_converter('usd', 'eur', balance)
    other_accounts = transactions.alternate_accounts(username, acct_number)
    print "\n\nAccount Number: {0}\tType: {1}".format(acct_number, acct_type)
    print "Account Owner: {0}".format(name)
    print "Username: {0}".format(username)
    print "Email: {0}".format(email)
    if currency == "usd":
        print "Account Number {0} has a balance of ${1:.2f}".format(acct_number, balance)
    else:
        balance = float(balance)
        print "Account Number {0} has a balance of €{1:.2f}".format(acct_number, balance)
    print "Alternate Accounts:"
    if other_accounts != '':
        for row in other_accounts:
            balance = transactions.compute_balance(row[0])
            if currency == "eur":
                balance = transactions.currency_converter('usd', 'eur', balance)
                balance = float(balance)
            if row[1] == "C":
                account_type = "Checking"
            else:
                account_type = "Savings"
            if currency == "usd":
                print "\tAccount Number: {0}\tType: {1}\tBalance: ${2:.2f}" \
                    .format(row[0], account_type, balance)
            else:
                print "\tAccount Number: {0}\tType: {1}\tBalance: €{2:.2f}" \
                    .format(row[0], account_type, balance)
    else:
        print "None"
    selection = 0
    while selection != 1 and selection != 2 and selection != 3 and selection != 4:
        print "\n\nPlease select a field to modify:\n\n"
        print "1. Account Type"
        print "2. Account Owner"
        print "3. Email"
        print "4. Password"
        selection = raw_input("\n\nPlease enter your selection:  ").strip()
        if selection.isdigit():
            selection = int(selection)
        if selection != 1 and selection != 2 and selection != 3 and selection != 4:
            print "\n\n#####################################################"
            print "###                                               ###"
            print "###         YOU ENTERED AN INVALID OPTION!        ###"
            print "###                                               ###"
            print "#####################################################\n\n"
        else:
            if selection == 1:
                transactions.modify_account_type(admin_username, acct_number)
            elif selection == 2:
                transactions.modify_account_owner(admin_username, acct_number)
            elif selection == 3:
                transactions.modify_account_email(admin_username, acct_number)
            elif selection == 4:
                transactions.modify_account_password(admin_username, acct_number)
    admin_home(admin_username, admin_name, currency)


##############################################################
##Teller Functions
def create_teller(admin_username, admin_name, currency):
    """Create New Teller"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                 Create Teller                 ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    teller_name = raw_input("Please enter the Teller's name:  ")
    while not all(x.isalpha() or x.isspace() for x in teller_name):
        teller_name = raw_input("Please enter a valid Teller's name:  ")
    teller_number = login.create_new_teller(teller_name, admin_username)
    print "The teller number for {0} is {1}.  Please make note of this number!" \
        .format(teller_name, teller_number)
    raw_input("\nPress <enter> to continue")
    admin_home(admin_username, admin_name, currency)


def bank_teller():
    """Bank Teller Welcome Screen"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###              Welcome Bank Teller              ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    teller_name = ''
    teller_number = ''
    while teller_name == '':
        teller_number = raw_input("Please enter your teller number:  ")
        if teller_number.isdigit():
            teller_name = login.teller_login(teller_number)
        else:
            print "\nPlease enter a numeric teller number!"
    if teller_name != '':
        teller_home(teller_name, teller_number, 'usd')


def teller_home(teller_name, teller_number, currency):
    """Home page for teller after login"""
    before_name = math.ceil((40 - len(teller_name)) / 2)
    after_name = math.floor((39 - len(teller_name)) / 2)
    before = ''
    after = ''
    while before_name > 0:
        before += ' '
        before_name -= 1
    while after_name > 0:
        after += ' '
        after_name -= 1

    print "\n\n#####################################################"
    print "###                                               ###"
    print "###{0}Welcome {1}{2}###".format(before, teller_name, after)
    print "###                                               ###"
    print "#####################################################\n\n"

    selection = 0
    while selection != 1 and selection != 2 and selection != 3 and selection != 4 \
            and selection != 5 and selection != 6:
        print "Please select from the following options:\n\n"
        print "1. View Account"
        print "2. Withdrawal"
        print "3. Deposit"
        print "4. Transfer"
        if currency == 'usd':
            print "5. Use Euro Currency"
        else:
            print "5. Use USD Currency"
        print "6. Logout\n\n"
        selection = raw_input("Please enter your selection:  ").strip()
        if selection.isdigit():
            selection = int(selection)
        if selection != 1 and selection != 2 and selection != 3 and selection != 4 \
                and selection != 5 and selection != 6:
            print "\n\n#####################################################"
            print "###                                               ###"
            print "###         YOU ENTERED AN INVALID OPTION!        ###"
            print "###                                               ###"
            print "#####################################################\n\n"
        else:
            if selection == 1:
                view_funds_screen(teller_name, teller_number, currency, 'Teller')
            elif selection == 2:
                withdrawal_screen(teller_name, teller_number, currency)
            elif selection == 3:
                deposit_screen(teller_name, teller_number, currency)
            elif selection == 4:
                transfer_screen(teller_name, teller_number, currency)
            elif selection == 5:
                if currency == 'usd':
                    currency = 'eur'
                else:
                    currency = 'usd'
                teller_home(teller_name, teller_number, currency)
            elif selection == 6:
                print "\n\n"
                home_screen()


## view_funds_screen() is implement in the System Admin functions above, it is also called by the teller role

def withdrawal_screen(teller_name, teller_number, currency):
    """Withdrawal screen for tellers"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                Withdraw Funds                 ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    acct_number = raw_input("Please enter an account number:  ")
    if acct_number.isdigit():
        acct_exists = transactions.valid_account(acct_number)
    else:
        acct_exists = 0
    while acct_exists == 0:
        print "That is not a valid account number!"
        acct_number = raw_input("Please enter an account number:  ")
        if acct_number.isdigit():
            acct_exists = transactions.valid_account(int(acct_number.strip()))
    amount = raw_input("Amount to withdraw: ")
    regex = re.compile(r"^[\d]+?\.[\d]{2}$")
    while not regex.match(amount):
        print "Please enter a valid monetary value"
        amount = raw_input("Amount to withdraw: ")
    amount = float(amount)
    if currency == "eur":
        amount = transactions.currency_converter('eur', 'usd', amount)
    amount = round(amount, 2)
    funds_available = transactions.verify_funds(acct_number, amount)
    if funds_available == 1:
        transactions.withdraw(acct_number, -amount)
        if currency == "usd":
            print "\n\n${0:.2f} has been withdrawn from account number: {1}" \
                .format(amount, acct_number)
        else:
            amount = transactions.currency_converter('usd', 'eur', amount)
            print "\n\n€{0:.2f} has been withdrawn from account number: {1}" \
                .format(amount, acct_number)
    else:
        if currency == "usd":
            print "\n\nThere are not available funds to withdraw ${0:.2f} from account number {1}" \
                .format(amount, acct_number)
        else:
            amount = transactions.currency_converter('usd', 'eur', amount)
            print "\n\nThere are not available funds to withdraw €{0:.2f} from account number {1}" \
                .format(amount, acct_number)
    raw_input("\nPress <enter> to continue")
    teller_home(teller_name, teller_number, currency)


def deposit_screen(teller_name, teller_number, currency):
    """Deposit screen for tellers"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                 Deposit Funds                 ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    acct_number = raw_input("Please enter an account number:  ")
    if acct_number.isdigit():
        acct_exists = transactions.valid_account(acct_number)
    else:
        acct_exists = 0
    while acct_exists == 0:
        print "That is not a valid account number!"
        acct_number = raw_input("Please enter an account number:  ")
        if acct_number.isdigit():
            acct_exists = transactions.valid_account(int(acct_number.strip()))
    amount = raw_input("Amount to deposit: ")
    regex = re.compile(r"^[\d]+?\.[\d]{2}$")
    while not regex.match(amount):
        print "Please enter a valid monetary value"
        amount = raw_input("Amount to deposit: ")
    amount = float(amount)
    if currency == "eur":
        amount = transactions.currency_converter('eur', 'usd', amount)
    amount = round(amount, 2)
    transactions.deposit(acct_number, amount)
    if currency == "usd":
        print "\n\n${0:.2f} has been deposited into account number: {1}".format(amount, acct_number)
    else:
        amount = transactions.currency_converter('usd', 'eur', amount)
        print "\n\n€{0:.2f} has been deposited into account number: {1}".format(amount, acct_number)
    raw_input("\nPress <enter> to continue")
    teller_home(teller_name, teller_number, currency)


def transfer_screen(teller_name, teller_number, currency):
    """Transfer screen for tellers"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                Transfer Funds                 ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    acct_number_withdraw = raw_input("Please enter an account number for withdrawal:  ")
    if acct_number_withdraw.isdigit():
        acct_1_exists = transactions.valid_account(acct_number_withdraw)
    else:
        acct_1_exists = 0
    while acct_1_exists == 0:
        print "That is not a valid account number!"
        acct_number_withdraw = raw_input("Please enter an account number for withdrawal:  ")
        if acct_number_withdraw.isdigit():
            acct_1_exists = transactions.valid_account(int(acct_number_withdraw.strip()))
    acct_number_deposit = raw_input("Please enter an account number for deposit:  ")
    if acct_number_deposit.isdigit():
        acct_2_exists = transactions.valid_account(acct_number_deposit)
    else:
        acct_2_exists = 0
    while acct_2_exists == 0:
        print "That is not a valid account number!"
        acct_number_deposit = raw_input("Please enter an account number for deposit:  ")
        if acct_number_deposit.isdigit():
            acct_2_exists = transactions.valid_account(int(acct_number_deposit.strip()))
    amount = raw_input("Amount to transfer: ")
    regex = re.compile(r"^[\d]+?\.[\d]{2}$")
    while not regex.match(amount):
        print "Please enter a valid monetary value"
        amount = raw_input("Amount to deposit: ")
    amount = float(amount)
    if currency == "eur":
        amount = transactions.currency_converter('eur', 'usd', amount)
    amount = round(amount, 2)
    funds_available = transactions.verify_funds(acct_number_withdraw, amount)
    if funds_available == 1:
        transactions.withdraw(acct_number_withdraw, -amount)
        transactions.deposit(acct_number_deposit, amount)
        if currency == 'usd':
            print "\n\n${0:.2f} has been transferred from account number: {1} to " \
                  "account number: {2}".format(amount, acct_number_withdraw, acct_number_deposit)
        else:
            amount = transactions.currency_converter('usd', 'eur', amount)
            print "\n\n€{0:.2f} has been transferred from account number: {1} to " \
                  "account number: {2}".format(amount, acct_number_withdraw, acct_number_deposit)
    else:
        if currency == 'usd':
            print"\n\nThere are not available funds to withdraw ${0:.2f} from account number {1}" \
                .format(amount, acct_number_withdraw)
        else:
            amount = transactions.currency_converter('usd', 'eur', amount)
            print"\n\nThere are not available funds to withdraw €{0:.2f} from account number {1}" \
                .format(amount, acct_number_withdraw)
    raw_input("\nPress <enter> to continue")
    teller_home(teller_name, teller_number, currency)


###############################################################
##User Functions
def user():
    """User Welcome Screen"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                 Welcome User                  ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    user_selection = ''
    while user_selection != 'y' and user_selection != 'n':
        print "Are you a new user?"
        user_selection = raw_input("(Y)es or (N)o? ").strip().lower()
        if user_selection == 'y':
            new_user()
        elif user_selection == 'n':
            old_user()


def new_user():
    """Screen for new users"""
    print "Welcome New User!"
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
        username = raw_input("Please enter your username: ")
        username_check = login.check_username(username)
        if username_check == 1:
            print "Username is in use.  Please select another!"
    password = getpass.getpass("Please enter your password: ")

    password = password_check(password)
    success = login.create_user(username, password, email, name)
    if success == 1:
        user_home(username)
    else:
        print "There was an error! Please try again."
        home_screen()


def old_user():
    """Screen for old users to login"""
    user_username = raw_input("Please enter your username:  ")
    user_password = getpass.getpass("Please enter your password:  ")
    login_result = login.user_login(user_username, user_password)
    user_input = ""
    if login_result == '':
        while user_input != "y" and user_input != "n":
            user_input = raw_input("incorrect login information. Try Again? (y)es or (n)o:  ").lower()
        if user_input == "n":
            home_screen()
        elif user_input == "y":
            old_user()
    else:
        user_home(user_username)


def user_home(username):
    """User home page after login"""
    before_name = math.ceil((40 - len(username)) / 2)
    after_name = math.floor((39 - len(username)) / 2)
    before = ''
    after = ''
    while before_name > 0:
        before += ' '
        before_name -= 1
    while after_name > 0:
        after += ' '
        after_name -= 1

    print "\n\n#####################################################"
    print "###                                               ###"
    print "###{0}Welcome {1}{2}###".format(before, username, after)
    print "###                                               ###"
    print "#####################################################\n\n"
    while True:
        print "Please select from the following options:\n\n"
        print "1. View Account"
        print "2. Withdrawal"
        print "3. Transfer"
        print "4. Open New Account"
        print "5. Change Username"
        print "6. Change Password"
        print "7. Logout\n\n"
        selection = raw_input("Please enter your selection:  ").strip()
        if selection.isdigit():
            selection = int(selection)
        if selection != 1 and selection != 2 and selection != 3 and selection != 4 \
                and selection != 5 and selection != 6:
            print "\n\n#####################################################"
            print "###                                               ###"
            print "###         YOU ENTERED AN INVALID OPTION!        ###"
            print "###                                               ###"
            print "#####################################################\n\n"
        elif selection == 1:  # add function calls here
            currency = 'usd'
            view_user_screen(currency)
        elif selection == 2:  # add function calls here
            acct_num = raw_input("Please enter the account number you wish to withdraw from: ").strip()
            if acct_num.isdigit():
                acct_num = int(acct_num)
            amount = raw_input("Please enter amount: ")
            if amount.isdigit():
                amount = int(amount)
            transactions.withdraw(acct_num, amount)
        elif selection == 3:  # add function calls here
            acct_num_from = raw_input("Account number to transfer from: ")
            if acct_num_from.isdigit():
                acct_num_from = int(acct_num_from)
            acct_num_to = raw_input("Account number to transfer to: ")
            if acct_num_to.isdigit():
                acct_num_to = int(acct_num_to)
            amount = raw_input("How much would you like to transfer: ")
            if amount.isdigit():
                amount = int(amount)
            transactions.transfer(acct_num_from, acct_num_to, amount)
        elif selection == 4:  # add function calls here
            pass
        elif selection == 5:  # add function calls here
            print "Please verify your username and password"
            user_username = raw_input("Please enter your username:  ")
            user_password = getpass.getpass("Please enter your password:  ")
            login_result = login.user_login(user_username, user_password)
            user_input = ""
            if login_result == '':
                while user_input != "y" and user_input != "n":
                    user_input = raw_input("incorrect login information. Try Again? (y)es or (n)o:  ").lower()
                    if user_input == "n":
                        home_screen()
                    elif user_input == "y":
                        old_user()
            else:
                new_username = raw_input("Change username to: ")
                transactions.change_username(user_username, new_username)
        elif selection == 6:
            print "Please verify your username and password"
            user_username = raw_input("Please enter your username:  ")
            user_password = getpass.getpass("Please enter your password:  ")
            login_result = login.user_login(user_username, user_password)
            user_input = ""
            if login_result == '':
                while user_input != "y" and user_input != "n":
                    user_input = raw_input("incorrect login information. Try Again? (y)es or (n)o:  ").lower()
                    if user_input == "n":
                        home_screen()
                    elif user_input == "y":
                        old_user()
            else:
                transactions.change_user_password(username)
        elif selection == 7:
            home_screen()


def view_user_screen(currency):
    """View account for tellers and admins"""
    print "\n\n#####################################################"
    print "###                                               ###"
    print "###                 View Account                  ###"
    print "###                                               ###"
    print "#####################################################\n\n"
    acct_number = raw_input("Please enter an account number:  ")
    if acct_number.isdigit():
        acct_exists = transactions.valid_account(acct_number)
    else:
        acct_exists = 0
    while acct_exists == 0:
        print "That is not a valid account number!"
        acct_number = raw_input("Please enter an account number:  ")
        if acct_number.isdigit():
            acct_exists = transactions.valid_account(int(acct_number.strip()))
    name = transactions.account_owner(acct_number)
    username = transactions.get_username(acct_number)
    balance = transactions.compute_balance(acct_number)
    if currency == "eur":
        balance = transactions.currency_converter('usd', 'eur', balance)
    other_accounts = transactions.alternate_accounts(username, acct_number)
    print "\n\nAccount Number: {0}".format(acct_number)
    print "Account Owner: {0}".format(name)
    print "Username: {0}".format(username)
    if currency == "usd":
        print "Account Number {0} has a balance of ${1:.2f}".format(acct_number, balance)
    else:
        balance = float(balance)
        print "Account Number {0} has a balance of €{1:.2f}".format(acct_number, balance)
    print "Alternate Accounts:"
    if other_accounts != '':
        for row in other_accounts:
            balance = transactions.compute_balance(row[0])
            if currency == "eur":
                balance = transactions.currency_converter('usd', 'eur', balance)
                balance = float(balance)
            if row[1] == "C":
                account_type = "Checking"
            else:
                account_type = "Savings"
            if currency == "usd":
                print "\tAccount Number: {0}\tType: {1}\tBalance: ${2:.2f}" \
                    .format(row[0], account_type, balance)
            else:
                print "\tAccount Number: {0}\tType: {1}\tBalance: €{2:.2f}" \
                    .format(row[0], account_type, balance)
    else:
        print "None"


def password_check(password):
    """Check for password length"""
    if len(password) < 6 or password.isupper() or password.islower() or password.isdigit():
        print "Passwords need to be at least 6 long, with upper and lowercase characters, and a number"
        password = getpass.getpass("Please enter again: ")
        password_check(password)
    else:
        print "Password Saved"
        return password
