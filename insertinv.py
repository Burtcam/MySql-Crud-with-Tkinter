from Errordialog import *
import pymysql as mdb
from tkinter import *
from tkinter.ttk import Combobox
from python_mysql_dbconfig import read_db_config


def getitems():

    query = "SELECT itemID FROM masteritem"

    connectionstring = read_db_config()
    con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'), connectionstring.get('password'),
                      connectionstring.get('database'))

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(query)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
    con.close()
    return result

def insertinv():
    result = getitems()
    #terms id, discount, days to earn, allowance

    window = Tk()
    window.title("Add a new inventory item")

    # ITEM ID
    itemidlbl = Label(window, text="New Item ID (Leave blank for no change)")
    itemidlbl.pack()
    itemid = Combobox(window)
    itemid.pack()
    itemid['values'] = result

    # QTY
    newqtylbl = Label(window, text="New Qty")
    newqtylbl.pack()
    newqty = Entry(window, width=10)
    newqty.pack()

    # LOCATION
    locationlbl = Label(window, text="New Location (Leave blank if no change)")
    locationlbl.pack()
    loc = Entry(window, width=10)
    loc.pack()

    def runinsertquery():
        itemid2 = "'" + itemid.get() + "'"
        qty = str(newqty.get())
        location = "'" + loc.get() + "'"

        #INSERT into inventory (itemID, onhand, location) VALUES ('I11000', 50, 'loc1')

        query = "INSERT into inventory (itemID, onhand, location) VALUES (" + itemid2 + "," + qty + "," + location +");"
        connectionstring = read_db_config()
        con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'), connectionstring.get('password'),
                          connectionstring.get('database'))
        try:
            with con:
                cur = con.cursor()
                cur.execute(query)

            con.close()
            itemid.delete(0, END)
            newqty.delete(0, END)
            loc.delete(0, END)
            good = success()

        except:
            itemid.delete(0, END)
            newqty.delete(0, END)
            loc.delete(0, END)
            fail = error()

    submitbtn = Button(window, text="Submit", command=runinsertquery)
    submitbtn.pack()
