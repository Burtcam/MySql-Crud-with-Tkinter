from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *

def getline(orderid, lineid):
    string = "SELECT * from lineitem where orderid = " +str(orderid) + " and lineID =" +str(lineid) +";"
    #print(string)

    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(string)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
    con.close()
    return result[0]


def costrecalc(orderid):
    #SELECT sum(cost) from lineitem where orderID = 36;
    string = "Select sum(cost) from lineitem where orderID = " + str(orderid) + ";"
    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(string)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
    con.close()
    #update orderheader set cost = BLANK where orderID = BLANK
    string = "update orderheader set cost = " +str(result[0][0]) + "where orderID = " + str(orderid) + ";"
    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(string)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
    con.close()




def costget(item, vendor):
    item = "'" +item + "'"
    string = "select cost from masteritem where itemID = " + item + " and vendorId = " + vendor + ";"
    #print(string)
    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

    # With will close the connection after the code is done,
     # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(string)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
    con.close()
   # print(result[0][0])
    return result[0][0]



def getvendor(orderid):
    #select vendorID from orderheader where orderID = 36;
    string = "SELECT vendorID from orderheader where orderID = " +str(orderid) + ";"

    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(string)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
        result = cur.fetchall()
    con.close()
    return result[0][0]


def updatelines():
    #ask for the order number and line number
    window = Tk()
    window.title("Update Lines")

    orderlbl = Label(window, text= "OrderID")
    orderlbl.pack()
    order = Entry(window, width = 10)
    order.pack()


    linelbl = Label(window, text = "Line Number")
    linelbl.pack()
    lineid = Entry(window, width= 10)
    lineid.pack()

    qtylbl = Label(window, text ="New Quantity")
    qtylbl.pack()
    qty = Entry(window, width = 10)
    qty.pack()

    def pushchange():
        #get line
        linek = lineid.get()
        orderid = order.get()
        orderline = getline(orderid, linek)

        #getvendor
        vend = getvendor(orderid)
        vend = "'" + vend +"'"

        #get cost
        cost = costget(orderline[1], vend)
        cost = cost*float(qty.get())

        #pushupdate
# #UPDATE lineitem
#SET itemid = value1, quantity = value2, cost =
#WHERE lineid =  and orderid = ;
        string = "UPDATE lineitem SET quantity = " +str(qty.get()) + ", cost = "+str(cost)+ " where lineid =" + str(linek) + " and orderid = " + str(orderid) + ";"
        con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');
        try:
            with con:
                cur = con.cursor()
                cur.execute(string)

            con.close()
            order.delete(0, END)
            lineid.delete(0, END)
            qty.delete(0, END)
        #update the order header
            costrecalc(orderid)
            good = success()

        except:
            order.delete(0, END)
            lineid.delete(0, END)
            qty.delete(0, END)
            fail = error()



    submit = Button(window, text = "Submit", command =pushchange)
    submit.pack()


    #ask for what needs to be changed

    #change it