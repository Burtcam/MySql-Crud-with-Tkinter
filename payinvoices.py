from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *
def getpaymentamount(invID):
    string= "Select amountpaid from masterinvoice where invoiceID = " +str(invID) + ";"
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




def payinvoices():
    window = Tk()
    window.title("Invoice Payment")
    window.geometry("640x640")

    #get invoice id
    invoiceidlbl= Label(window, text= "Invoice ID")
    invoiceidlbl.pack()
    invoice = Entry(window, width= 10)
    invoice.pack()

    #get payment amount
    paymentlbl = Label(window,text="Payment Amount")
    paymentlbl.pack()
    pay = Entry(window, width=10)
    pay.pack()

    #apply
    def push():
        payed = getpaymentamount(invoice.get())
        payed = float(payed) + float(pay.get())
        string = "update masterinvoice set amountpaid = " + str(payed) + " where invoiceID = " + str(invoice.get()) + ";"
        con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');
        try:
            with con:
                cur = con.cursor()
                cur.execute(string)

            con.close()
            invoice.delete(0, END)
            pay.delete(0, END)
            good = success()
        except:
            invoice.delete(0, END)
            pay.delete(0, END)
            fail = error()

    submit = Button(window, text="Submit Payment", command=push)
    submit.pack()