from tkinter import *
from addmasteritem import additem
from newvendor import addvendor
import pymysql as mdb
from inserttermscodes import addatermscode
from viewinv import viewinv
from putawayinv import updateinv
from delete import deleteinv
from insertinv import insertinv
from addorder import addorder
from updatelines import updatelines
from updateorder import updateorder
from vieworders import openorders
from insertinvoice import insertinvoice
from viewinvoices import viewinvoices
from payinvoices import payinvoices



def addanitembtn():
    additem()

def addvendorbtn():
    addvendor()

def main():
    window = Tk()

    window.title("Welcome to the LivePlay system")
    window.geometry("640x640")
    def exit():
        window.destroy()

    #Basetable management Banner
    basetbllbl = Label(window, text="Base Table Management", font=("Helvetica", 16))
    basetbllbl.pack()

    #INSERT item
    additembtn = Button(window, text="Add a new item", command=addanitembtn)
    additembtn.pack()

    #insert vendor
    insertvendorbtn = Button(window, text = "Register a new vendor", command=addvendorbtn)
    insertvendorbtn.pack()

    #insert terms codes
    inserttermsbtn = Button(window, text = "Insert Terms", command= addatermscode)
    inserttermsbtn.pack()

    # Basetable management Banner
    invmanglbl = Label(window, text="Inventory Management", font=("Helvetica", 16))
    invmanglbl.pack()

    #insert inventory
    insertinventorybtn = Button(window, text="Putaway Inventory", command=insertinv)
    insertinventorybtn.pack()

    #View Inventory
    viewinventorybtn = Button(window, text ="View Inventory", command =viewinv)
    viewinventorybtn.pack()

    #update inventory
    updatebtn = Button(window, text="Update Inventory", command=updateinv)
    updatebtn.pack()

    #Delete inventory
    deleteinvbtn = Button(window, text = "Delete Inventory", command = deleteinv)
    deleteinvbtn.pack()

    # Order management Banner
    ordermanglbl = Label(window, text="Order Management", font=("Helvetica", 16))
    ordermanglbl.pack()

    #insert order
    addorderbtn = Button(window, text ="Add a New Order/Add Lines", command = addorder)
    addorderbtn.pack()

    updatelinesbtn = Button(window, text ="Update Existing Lines", command =updatelines)
    updatelinesbtn.pack()

    #mark orders as in transit or as recieved (update)
    updateordersbtn = Button(window, text= "Update Order Header", command =updateorder)
    updateordersbtn.pack()

    #view Orders
    openordersbtn = Button(window, text="View Open Orders", command=openorders)
    openordersbtn.pack()

    # Order management Banner
    invoicemanglbl = Label(window, text="Invoice Management", font=("Helvetica", 16))
    invoicemanglbl.pack()

    #insertinvoice
    insertinvoicebtn = Button(window, text="Log Invoices", command=insertinvoice)
    insertinvoicebtn.pack()

    #viewinvoices
    viewinvoicesbtn = Button(window, text="Query Invoices", command =viewinvoices)
    viewinvoicesbtn.pack()

    #payinvoices
    payinvoicebtn = Button(window, text="Pay Invoices", command = payinvoices)
    payinvoicebtn.pack()

    Killmyselfbtn = Button(window, text="Exit", command=exit)
    Killmyselfbtn.pack()


    window.mainloop()

main()