from tkinter import *
from tkinter.ttk import Combobox, Treeview
import pymysql as mdb
from Errordialog import *



def getinvoices():
    string = "select * from masterinvoice"
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
    print(result)
    return result


def viewinvoices():
    window = Tk()
    window.title("View Invoices")

    result = getinvoices()
    print(result)
    tree = Treeview(window, columns=('Invoice ID', 'Date Logged', 'Payment Due Date', 'Total Due', 'VendorID', 'Paid to Date'), show='headings')

    tree.heading('Invoice ID', text="Invoice ID")
    tree.heading('Date Logged', text="Date Logged")
    tree.heading('Payment Due Date', text="Payment Due Date")
    tree.heading('Total Due', text="Total Due")
    tree.heading('VendorID', text="VendorID")
    tree.heading('Paid to Date', text="Paid to Date")
    tree.pack()

    for i in range(len(result)):
        tree.insert("", "end", values=(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4], result[i][5]))
