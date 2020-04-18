from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *



def getitems():

    query = "SELECT itemID FROM masteritem"

    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(query)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
        return result
    con.close()


