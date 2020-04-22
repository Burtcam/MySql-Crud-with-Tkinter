from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *
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

def getline(x):

    query = "SELECT * FROM inventory where recordnum =" + str(x) + ";"

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

def updateinv():
    result = getitems()
    window = Tk()
    window.title("Update inventory")

    #REC NUM
    toupdatereclbl = Label(window, text = "Record Num to update")
    toupdatereclbl.pack()
    recnum = Entry(window, width = 10)
    recnum.pack()

    #ITEM ID
    itemidlbl = Label(window, text = "New Item ID (Leave blank for no change)")
    itemidlbl.pack()
    itemid = Combobox(window)
    itemid.pack()
    itemid['values'] = result

    #QTY
    newqtylbl = Label(window, text = "New Qty")
    newqtylbl.pack()
    newqty = Entry(window, width = 10)
    newqty.pack()

    #LOCATION
    locationlbl = Label(window, text = "New Location (Leave blank if no change)")
    locationlbl.pack()
    loc = Entry(window, width = 10)
    loc.pack()


    def runputaway():
        location = loc.get()
        qty = newqty.get()
        item = itemid.get()
        rec = recnum.get()

        # 1. that the Rec num is a num and is accurate

        try:
            rec = int(rec)
        except ValueError:
            print("Invalid Record Number")
        #get the current info
        result = getline(rec)

        #input validation goals:


        #2. determine what is there to change

        if location is "":
            location = result[0][3]
        if item is "":
            item = result[0][1]


        query = "UPDATE inventory SET location = '" + location + "' ,onhand = " + str(qty) + " ,itemID = '" + item + "' WHERE recordnum = " + str(rec) +";"
        #Actually build the string and run it
        connectionstring = read_db_config()
        con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'), connectionstring.get('password'),
                          connectionstring.get('database'))
        try:
            with con:
                cur = con.cursor()
                cur.execute(query)

            con.close()
            loc.delete(0, END)
            newqty.delete(0, END)
            itemid.delete(0, END)
            recnum.delete(0, END)
            good = success()
        except:
            loc.delete(0, END)
            newqty.delete(0, END)
            itemid.delete(0, END)
            recnum.delete(0, END)
            fail = error()


    #submit button
    submitbtn = Button(window, text="Submit", command=runputaway)
    submitbtn.pack()






