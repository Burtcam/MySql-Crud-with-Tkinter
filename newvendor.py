from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *



def getterms():

    query = "SELECT termsID FROM termscodes"

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

def addvendor():
    termscodes = getterms()
    #vendor id, contact name, vendorname, country, state, zip, address terms id * foreign key
    window = Tk()
    window.title("Add a New Vendor")

    #vendor ID
    vendoridlbl = Label(window, text="New vendorID")
    vendoridlbl.grid(column=0, row=0)
    newvendorid = Entry(window, width=10)
    newvendorid.grid(column=1, row=0)


    #contact name
    contactlbl = Label(window, text="Contact Name (first and last)")
    contactlbl.grid(column=2, row=0)
    contact = Entry(window, width=10)
    contact.grid(column=3, row=0)

    #vendor business name
    vendornamelbl = Label(window, text="Full Vendor Name")
    vendornamelbl.grid(column=4,row=0)
    name = Entry(window,width = 10)
    name.grid(column=5,row=0)

    #country code
    countrycodelbl = Label(window, text="Country Code")
    countrycodelbl.grid(column=0,row=1)
    country = Combobox(window)
    country.grid(column=1, row=1)
    country['values'] = ("USA", "CHN", "IND")

    #state
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    statecodelbl = Label(window, text="State Code")
    statecodelbl.grid(column=2, row=1)
    statecombo = Combobox(window)
    statecombo.grid(column =3, row =1)
    statecombo['values'] = states

    #zipcode TODO input validation?
    ziplbl = Label(window, text= "ZipCode")
    ziplbl.grid(column=4, row= 1)
    zipent=Entry(window, width= 10)
    zipent.grid(column=5, row =1)

    #address
    addresslbl = Label(window, text="Address")
    addresslbl.grid(column=6,row=1)
    address = Entry(window, width = 50)
    address.grid(column=7,row=1)

    #terms code combo
    termscodelbl = Label(window, text="Terms Code")
    termscodelbl.grid(column=6, row=0)
    termscombo = Combobox(window)
    termscombo.grid(column=7, row=0)
    termscombo['values'] = termscodes

    # vendor id, contact name, vendorname, country, state, zip, address terms id * foreign key
    def runinsertquery():
        vendorid = "'"+ newvendorid.get() +"'"
        contactname = "'"+contact.get() + "'"
        vendor = "'"+name.get()+"'"
        countrycode = "'"+country.get()+"'"
        state = "'" + statecombo.get() +"'"
        zipcode = "'"+zipent.get() +"'"
        add = "'" + address.get() +"'"
        terms = "'"+termscombo.get()+"'"

        query = "Insert into mastervendor (vendorId,contactName,vendorName, country, state, zip, address, termsID) VALUES (" + vendorid + "," + contactname + "," +vendor + "," + countrycode + "," +state + ", " + zipcode + ", " + add + ", " + terms +");"
        con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');
        try:
            with con:
                cur = con.cursor()
                cur.execute(query)

            con.close()
            newvendorid.delete(0, END)
            contact.delete(0, END)
            name.delete(0, END)
            country.delete(0, END)
            statecombo.delete(0, END)
            zipent.delete(0, END)
            address.delete(0,END)
            termscombo.delete(0, END)
            good = success()
        except:
            newvendorid.delete(0, END)
            contact.delete(0, END)
            name.delete(0, END)
            country.delete(0, END)
            statecombo.delete(0, END)
            zipent.delete(0, END)
            address.delete(0, END)
            termscombo.delete(0, END)
            fail = error()





    #submit button
    submitbtn = Button(window, text="Submit", command=runinsertquery)
    submitbtn.grid(column=3, row=2)
