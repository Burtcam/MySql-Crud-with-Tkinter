from Errordialog import *
import pymysql as mdb
from tkinter import *
from python_mysql_dbconfig import read_db_config


def addatermscode():

    #terms id, discount, days to earn, allowance

    window = Tk()
    window.title("Add a new Terms Code")

    #terms code
    termslbl = Label(window, text = "TermsID")
    termslbl.pack()
    termscode = Entry(window, width = 10)
    termscode.pack()

    #discount amount
    discountlbl = Label(window, text ="Enter the discount (Percentage as a Decimal)")
    discountlbl.pack()
    discount = Entry(window, width =10)
    discount.pack()


    #daystoearn
    dayslbl = Label(window, text =" Days to Earn Discount")
    dayslbl.pack()
    days = Entry(window, width = 10)
    days.pack()

    #allowance
    allowancelbl = Label(window, text= "Allowance Amount (Percentage as a Decimal)")
    allowancelbl.pack()
    allowance = Entry(window, width = 10)
    allowance.pack()

    def runinsertquery():
        termscodes = "'" + termscode.get() + "'"
        discountamt = "'" + str(discount.get()) + "'"
        disc = discount.get()
        #print(disc)
        daystoearn = "'" +str(days.get())+"'"
        allowanceamt  = "'" + str(allowance.get()) + "'"

        query = "Insert into termscodes (termsID, discount, allowance, daystoearndiscount) VALUES (" + termscodes + "," + discountamt + "," + allowanceamt + "," + daystoearn +");"
        connectionstring = read_db_config()
        con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'), connectionstring.get('password'),
                          connectionstring.get('database'))
        try:
            with con:
                cur = con.cursor()
                cur.execute(query)

            con.close()
            allowance.delete(0, END)
            days.delete(0, END)
            termscode.delete(0, END)
            discount.delete(0, END)
            good = success()

        except:
            allowance.delete(0, END)
            days.delete(0, END)
            termscode.delete(0, END)
            discount.delete(0, END)
            fail = error()

    submitbtn = Button(window, text="Submit", command=runinsertquery)
    submitbtn.pack()
