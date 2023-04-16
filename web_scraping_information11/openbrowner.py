import sys, webbrowser

import pyperclip

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/search?q=" + address)
