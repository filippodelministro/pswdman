import sys
import os



OK_CODE = 1
n_pswd = 0

class pswd_object:
    def __init__(self, service, password):
        self.service = service
        self.password = password

list = []   # list of pswd_objects

# -----------------------------------------------
#                  UTILITY FUNCTIONS
# ----------------------------------------------- 

def prompt():
    print(">", end='')

# ----------------------------------------------- 
#                  COMMANDS FUNCTIONS
# ----------------------------------------------- 

def help_command():
    print("Try any of the following commands:\n\n"
        "1) help: show commands details\n"
        "2) list: show all passwprd list\n"
        "3) save: save new password\n"
    )

def boot_command():
    print("Welcome in pswdman!\n")
    help_command()

def esc_command():
    exit(0)

def list_command():
    print("\t#\tname\tpassword\n")

    i = 1
    for obj in list:
        print("\t" + str(i) + "\t" + obj.service + "\t\t" + obj.password)
        i += 1

def save_command():
    ok = False

    serv = input("Insert service you want to save a password for: \n")
    #todo: find service

    while not ok:
        psw = input("password: ")
        confirm = input("password confirm: ")

        if psw == confirm:
            ok = True
        else:
            print("password dont match: retry\n")

    list.append(pswd_object(serv, psw))

    return OK_CODE


def clear_command():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def read_command():
    prompt()
    cmd = input()

    if cmd in ("clear", "cls"):
        clear_command()
    elif cmd == "esc":
        esc_command()
    elif cmd == "help":
        help_command()
    elif cmd == "list":
        list_command()
    elif cmd == "save":
        save_command()
    else:
        print("Command not found!\n");
        help_command()
        


