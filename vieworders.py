from tkinter import *
from tkinter.ttk import Combobox, Treeview
import pymysql as mdb
from Errordialog import *
from python_mysql_dbconfig import read_db_config



def getorders():
    string = "select * from orderreport where orderreceived is NULL or shipdate is Null;"
    connectionstring = read_db_config()
    con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'), connectionstring.get('password'),
                      connectionstring.get('database'))

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


def openorders():
    window = Tk()
    window.title("View Inventory")

    result = getorders()
    # print(result)
    tree = Treeview(window, columns=('Line Key', 'Item ID', 'Quantity', 'Line Number', 'Order ID', 'Line Cost','Order Recieved', 'Vendor ID', 'Order Date', 'Ship Date'), show='headings')
    tree.heading('Line Key', text="Line Key")
    tree.heading('Item ID', text="Item ID")
    tree.heading('Quantity', text="Quantity")
    tree.heading('Line Number', text="Line Number")
    tree.heading('Order ID', text="Order ID")
    tree.heading('Line Cost', text="Line Cost")
    tree.heading('Order Recieved', text="Order Recieved")
    tree.heading('Vendor ID', text="Vendor ID")
    tree.heading('Order Date', text="Order Date")
    tree.heading('Ship Date', text="Ship Date")
    tree.pack()

    for i in range(len(result)):
        tree.insert("", "end", values=(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4], result[i][5], result[i][6],result[i][7], result[i][8], result[i][9]))
