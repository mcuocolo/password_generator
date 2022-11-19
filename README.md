# Password generator

## Description: 
This password generator is written in python. 
It's the starting point to put my python knowledge to the test.
Many more features will be added in future versions.

## How to use: 
# 1. Install dependencies

Dependencies for this program to run are detailed the following :
- pyperclip

You can add pyperclip with :

``` pip install pyperclip ```

# 2. Text interface
This program can be used as text interface only and in this case the only installation 
requirements is pyperclip that is used to copy the generated password to system memory.
In this case the following packages are required for this script to work.
- pyperclip 
- Flask
- qrcode

You can add these dependencies with :

``` pip install Flask, qrcode[pil], pyperclip ```

*Note : the qrcode[pil] command will also install **Python Imaging Library** 
in order to generate the qrcode images.*

To run the text only interface run : **main.py**

# 3. Webapp using Flask
The second option is to run app.py to bring a Flask generated webpage used as graphical interface.
The functionality is the same with the added generation of a qr code for quick copy to your smartphone.
Use the checkboxes to select password options.
To run the webapp run : **flask_app.py**

## Collaborators: 
I'm doing that on my own. Any comments or suggestions welcome

## License: 
MIT
*But seriously if you find that code useful in any way don't hesitate to send an email and say thanks of whatever...*
