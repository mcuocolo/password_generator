import pyperclip

""" export module to export generate password to :
 - clipboard
 - sms (not yet implemented)
 - twitter (not yet implemented)
 - secure vault (not yet implemented
 - future ideas ...
 """

def copy_to_clipboard(psw):
    """ function using pyperclip to save psw to clipboard """
    pyperclip.copy(psw)
    print("Password copied to clipboard")


