import pyperclip
import qrcode

""" export module to export generated password to :
 - clipboard
 - as a qr code
 - sms (not yet implemented)
 - twitter (not yet implemented)
 - secure vault (not yet implemented
 - future ideas ...
 """

def copy_to_clipboard(psw):
    """ function using pyperclip to save psw to clipboard """
    pyperclip.copy(psw)
    print("Password copied to clipboard")


def make_qr_code(psw):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=5,
    )
    qr.add_data(psw)
    img = qr.make_image(fill_color="#0080ff", back_color="white")
    img.save("static/img/qr_psw.png")