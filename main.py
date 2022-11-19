from utils.password import Password
from utils.export_psw import copy_to_clipboard
""" This is a basic "console input" implementation of the password module
Generate input requests to the console and calls the Password.generate_psw method 

NB: Temporary implementation used to test the Password class before moving to GUI and web versions
"""

def _get_length(password):
    """ function checks if password str casting to int doesn't generate an error """
    try:
        password.length = int(input("Choose psw length (int): "))
    except ValueError:
        print("Please input only an integer value")
        _get_length(password)
    except:
        print("Something went wrong, try again")
        _get_length(password)


def _get_input(option):
    """ function creates a loop until input is either a y or an n"""
    try:
        answer = input(f"Allow {option}? (y/n) : ")
        if answer == ("y" or "Y"):
            return True
        elif answer == ("n" or "N"):
            return False
        else:
            print("Please enter 'y/Y' or 'n/N'")
            _get_input(option)
    except:
        print("Something went wrong, try again")
        _get_input(option)


def run():
    """ basic call to password module """
    password = Password()
    _get_length(password)
    for item in vars(password).keys():
        if item == "length":
            break
        option = item.replace("allow_", "")
        vars(password)[item] = _get_input(option)

    result, msg, psw = password.generate_psw()
    print(f"Password generation success = {result}")
    print(msg)
    copy_to_clipboard(psw)


if __name__ == "__main__":
    run()
