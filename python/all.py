import sys
import os

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
    #todo

def save_command():
    print("Insert service you want to save a password for: \n")
    #todo:

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
        print("Unknown command, try one of below")
        help_command()
        


