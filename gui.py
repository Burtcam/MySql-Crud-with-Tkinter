from tkinter import *
from addmasteritem import additem
from newvendor import addvendor
import pymysql as mdb
from inserttermscodes import addatermscode
from viewinv import viewinv



def addanitembtn():
    additem()

def addvendorbtn():
    addvendor()

def main():
    window = Tk()

    window.title("Welcome to the gameshop system")

    window.geometry('540x540')


    #INSERT item
    additembtn = Button(window, text="Add a new item", command=addanitembtn)
    additembtn.pack()

    #insert vendor
    insertvendorbtn = Button(window, text = "Register a new vendor", command=addvendorbtn)
    insertvendorbtn.pack()

    #insert terms codes
    inserttermsbtn = Button(window, text = "Insert Terms", command= addatermscode)
    inserttermsbtn.pack()

    viewinventorybtn = Button(window, text ="View Inventory", command =viewinv)
    viewinventorybtn.pack()


    window.mainloop()

main()