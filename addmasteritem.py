from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *
from datetime import datetime
from python_mysql_dbconfig import read_db_config

def getvendors():

    query = "SELECT vendorID FROM mastervendor"

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
        return result
    con.close()




#popout a new window which allows for an insert statement to the db
def additem():
    def endfunc():
        return 0

    try:
        vendorlist = getvendors()
    except:
        window =Tk()
        window.title("No vendors!")
        okbtn = Button(window, text="OK", command=endfunc)
        okbtn.grid(column = 0, row = 0)


    window = Tk()
    window.title("Add a new item")

    itemidlbl = Label(window, text="New ItemID")
    itemidlbl.grid(column=0, row=0)

    newitemId = Entry(window, width=10)
    newitemId.grid(column=1, row=0)

    costlbl = Label(window,text="Cost")
    costlbl.grid(column=2,row=0)

    newcost = Entry(window,width=10)
    newcost.grid(column=3,row=0)

    #vendor combobox
    #get current list of vendors
    vendorlbl = Label(window,text="Choose a vendor")
    vendorlbl.grid(column=4,row=0)
    vendor = Combobox(window)
    vendor.grid(column=5,row=0)
    vendor['values'] = vendorlist

    def runinsertquery():
        # learn how to build a query that will send it to the DB and if successful reponds
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        formatted_date = "'" + formatted_date + "'"
        # bbuild string
        string = "Insert into masteritem (itemID,cost,vendorID, intialPurchaseDate) VALUES (" + "'" + newitemId.get() +"', '" + newcost.get() + "', '" + vendor.get() +"'," + formatted_date +");"
        connectionstring = read_db_config()
        con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'), connectionstring.get('password'), connectionstring.get('database'));

        try:
            with con:
                cur = con.cursor()
                cur.execute(string)

            con.close()
            newitemId.delete(0, END)
            newcost.delete(0, END)
            vendor.delete(0, END)
            good = success()

        except:
            newitemId.delete(0, END)
            newcost.delete(0, END)
            vendor.delete(0, END)
            fail = error()
    submitbtn  = Button(window, text="Submit", command=runinsertquery)
    submitbtn.grid(column=6,row=0)

    window.title("Add an item to the system")

    window.geometry('540x540')

    window.mainloop()

