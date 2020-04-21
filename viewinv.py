from tkinter import *
from tkinter.ttk import Combobox, Treeview
import pymysql as mdb
from Errordialog import *


def getinv():
    string = "Select recordnum,itemid, onhand, location From inventory;"
    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(string)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
        return result
    con.close()


def viewinv():
    window = Tk()
    window.title("View Inventory")

    result = getinv()
   # print(result)
    tree = Treeview(window, columns=('Record Num','Item ID', 'On Hand', 'Location'), show='headings')
    tree.heading('Record Num', text = "Record Number")
    tree.heading('Item ID', text = "Item ID")
    tree.heading('On Hand', text ="On Hand")
    tree.heading('Location', text = "Location")
    tree.pack()

    for i in range(len(result)):
        tree.insert("", "end", values=(result[i][0], result[i][1], result[i][2], result[i][3]))





