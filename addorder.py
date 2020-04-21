from Errordialog import *
import pymysql as mdb
from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
from tkinter import messagebox



def getordercost(orderid):
    string = "select cost from orderheader where orderID =" + str(orderid) +";"
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


def costget(item, vendor):
    string = "select cost from masteritem where itemID = " +item +"and vendorId = " + vendor +";"
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
    #print(result[0][0])
    return result[0][0]

def findorder():
    string = "select max(orderID) from orderheader;"
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
    #print(result[0][0])
    return result[0][0]

def findlineid(order):
    string = "select max(lineID) from lineitem where orderid = " +str(order) +";"
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
    return result



def getitems(vendor):

    query = "SELECT itemID FROM masteritem where vendorid = "+ vendor +";"

    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

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

def getvendors():

    query = "SELECT vendorID FROM mastervendor"

    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

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

def getterms(vendor):
    query = "select termsID from mastervendor where vendorid =" + "'" +vendor+"';"
    con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

    # With will close the connection after the code is done,
    # regardless of how the code exists. Use as an alternative to 'finally' statement
    with con:
        cur = con.cursor()
        cur.execute(query)

        # Get all of the MySQL return at once
        # Returns a tuple of tuples, with each inner tupple being one row
    result = cur.fetchall()
    con.close()
    return result[0][0]



def addorder():
    #open window and prompt for information
    vendorlist = getvendors()
    window = Tk()
    window.title("Add a new Order")

    # vendor combobox
    # get current list of vendors
    vendorlbl = Label(window, text="Choose a vendor")
    vendorlbl.pack()
    vendor = Combobox(window)
    vendor.pack()
    vendor['values'] = vendorlist

    #new order
    neworderlbl = Label(window, text = "New order?")
    neworderlbl.pack()
    neworder = Combobox(window)
    neworder.pack()
    neworder['values'] = ('Yes', 'No')



    #orderID
    def updateordercheck():
        def addnew():
            # will start loop to add a totally new order and lines
            #write order header
            #vendor, orderid(AUTO), orderDate(DATE), cost = 0, termsid
            vend = "'"+ vendor.get()+"'"
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            cost = 0
            terms = "'"+getterms(vendor.get()) +"'"
            query = "insert into orderheader(vendorid, orderdate, cost, termsid) VALUES ("+vend+"," +"'" +formatted_date +"'" +","+str(cost)+","+terms+");"


            con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

            # With will close the connection after the code is done,
            # regardless of how the code exists. Use as an alternative to 'finally' statement
            with con:
                cur = con.cursor()
                cur.execute(query)
            con.close()


            def pushline():
                # line id

                # order id#use max
                orderID = findorder()

                # line id
                line = findlineid(orderID)
                if line[0][0] is None:
                    lineid = 1
                else:
                    lineid = line[0][0] + 1

                #actually insert line!
                itemID = "'"+item.get()+"'"
                cost = costget(itemID, vend)
                cost = cost * float(qty.get())
                string = "INSERT into lineitem (itemID, quantity, lineid, orderID, cost) VALUES (" +itemID + "," + str(qty.get()) + "," + str(lineid) + "," + str(orderID) + ","+ str(cost)+ ");"
               # print (string)
                con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

                # With will close the connection after the code is done,
                # regardless of how the code exists. Use as an alternative to 'finally' statement
                with con:
                    cur = con.cursor()
                    cur.execute(string)
                con.close()
            #push line info clear line input
                qty.delete(0, END)
                item.delete(0, END)

            #update cost of order header
                orderheadercost = getordercost(orderID)
               # print(orderheadercost)
                orderheadercost = orderheadercost + cost
                string = "update orderheader SET cost = " + str(orderheadercost) + "where orderID = " + str(orderID) + ";"
                con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

                # With will close the connection after the code is done,
                # regardless of how the code exists. Use as an alternative to 'finally' statement
                with con:
                    cur = con.cursor()
                    cur.execute(string)
                con.close()
                linewindow.destroy()

                messagebox.showinfo("Order Created", "Order ID: "+str(orderID)+" Created Succesfully")


            #get line info
            linewindow = Tk()
            linewindow.title("Add a line")

            #item id
            itemlist =getitems(vend)
            itemlbl = Label(linewindow, text = "Choose an item")
            itemlbl.pack()
            item = Combobox(linewindow)
            item.pack()
            item['values'] = itemlist

            #quantity
            qtylbl = Label(linewindow, text = "Quantity")
            qtylbl.pack()
            qty = Entry(linewindow, width = 10)
            qty.pack()

            #submit
            submit = Button(linewindow, text = "Push line", command =pushline)
            submit.pack()



                #UPDATE table_name
#SET column1 = value1, column2 = value2, ...
#WHERE condition;


        def updateorder():
            orderid = ordernum.get()
            linewindow = Tk()
            linewindow.title("Add a line")

            # item id
            itemlist = getitems("'"+vendor.get()+"'")
            itemlbl = Label(linewindow, text="Choose an item")
            itemlbl.pack()
            item = Combobox(linewindow)
            item.pack()
            item['values'] = itemlist

            # quantity
            qtylbl = Label(linewindow, text="Quantity")
            qtylbl.pack()
            qty = Entry(linewindow, width=10)
            qty.pack()

            def updateexisting():
                # get line info
                # line id
                line = findlineid(orderid)
                if line[0][0] is None:
                    lineid = 1
                else:
                    lineid = line[0][0] + 1

                # cost
                cost = costget("'" + item.get() + "'", "'" + vendor.get() + "'")
                cost = cost * float(qty.get())

                # push line info clear line input

                string = "INSERT into lineitem (itemID, quantity, lineid, orderID, cost) VALUES (" + "'"+str(item.get())+"'," + str(qty.get()) + "," + str(lineid) + "," + str(orderid) + "," + str(cost) + ");"
                #print (string)
                con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

                # With will close the connection after the code is done,
                # regardless of how the code exists. Use as an alternative to 'finally' statement
                with con:
                    cur = con.cursor()
                    cur.execute(string)
                con.close()
                # push line info clear line input
                qty.delete(0, END)
                item.delete(0, END)

                # update cost of order header
                orderheadercost = getordercost(orderid)
               # print(orderheadercost)
                orderheadercost = orderheadercost + cost
                string = "update orderheader SET cost = " + str(orderheadercost) + "where orderID = " + str(
                    orderid) + ";"
                con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop')

                # With will close the connection after the code is done,
                # regardless of how the code exists. Use as an alternative to 'finally' statement
                with con:
                    cur = con.cursor()
                    cur.execute(string)
                con.close()
                linewindow.destroy()
                succ = success()
            # get line info
            # line id
            submit = Button(linewindow, text="Push lines", command=updateexisting)
            submit.pack()

        if neworder.get() == 'No':
            ordernumlbl = Label(window, text="Order Number")
            ordernumlbl.pack()
            ordernum = Entry(window, width=10)
            ordernum.pack()
            sub = Button(window, text ="Submit and Add lines", command = updateorder)
            sub.pack()
        else:
            addnew()
            neworder.set('No')
        #if order ID exists, add line, else add order ID


    #addlines
    addlinesbtn = Button(window, text ="Add Line", command=updateordercheck)
    addlinesbtn.pack()



    #order date https://www.quora.com/How-do-I-insert-a-date-into-MySQL-using-Python


    #Order ID Autoincrement

    #terms id pulls from vendor






    #add line button opens a seperate window which will push the order the first time, and then take the data, add a new line on submit AND UPDATES COST ON ORDER HEADER

    #add a new order, clears order window and thus allows the process to start over