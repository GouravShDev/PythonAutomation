#! python3
import requests
import webbrowser
import pyperclip
import sys
from tkinter import *
from tkinter import messagebox 

def openBrowser(url):
    webbrowser.open(url)

def getClipboard():
    search = pyperclip.paste();
    return search

def getArgument():
    if len(sys.argv) > 1:
        search = ' '.join(sys.argv[1:])
    else:
        search = getClipboard()
    return search

def showErrorDialog():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    
    messagebox.showerror('Error','No input provided')
    
    window.deiconify()
    window.destroy()
    window.quit()
    
def main():
    url = "https://nyaa.si/?f=0&c=0_0&q=" + getArgument()+"&s=seeders&o=desc"
    if(len(getArgument()) == 0):
        showErrorDialog()
        sys.exit()
    openBrowser(url)
    
if __name__ == '__main__':
    main()