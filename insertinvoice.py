from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *
from addmasteritem import getvendors
from datetime import datetime
from python_mysql_dbconfig import read_db_config

def insertinvoice():

    window = Tk()
    window.title("Insert Invoice")

    #date received
    monthlbl = Label(window, text="Due Month")
    monthlbl.pack()
    month = Combobox(window)
    month.pack()
    month['values'] = ('01',
                       '02',
                       '03',
                       '04',
                       '05',
                       '06',
                       '07',
                       '08',
                       '09',
                       '10',
                       '11',
                       '12')
    daylbl = Label(window, text=" Due Day")
    daylbl.pack()

    daylist = []
    for i in range(1, 31):
        daylist.append(str(i));
    day = Combobox(window)
    day.pack()
    day['values'] = daylist

    yearlbl = Label(window, text="Due Year")
    yearlbl.pack()
    yearlist = []
    for i in range(1990, 2040):
        yearlist.append(str(i))
    year = Combobox(window)
    year.pack()
    year['values'] = yearlist

    # vendorID
    vendorlist = getvendors()
    vendorlbl = Label(window, text="Choose a vendor")
    vendorlbl.pack()
    vendor = Combobox(window)
    vendor.pack()
    vendor['values'] = vendorlist

    #Grossamount
    amtlbl = Label(window, text = "Enter an Amount")
    amtlbl.pack()
    amt = Entry(window, width = 10)
    amt.pack()

    def pushit():
        #yyyy-mm-dd
        datestring = "'"+str(year.get()) +"-" + str(month.get()) +"-" + str(day.get()) +"'"

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        formatted_date = "'" + formatted_date + "'"
        #INSERT INTO table_name(column1, column2, column3, ...)
        #VALUES(value1, value2, value3, ...);
        string = "Insert into masterinvoice(datereceived,paymentduedate,grossamount,vendorID) VALUES("+formatted_date+","+datestring+","+str(amt.get()) +", '" +vendor.get() +"');"

        connectionstring = read_db_config()
        con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'), connectionstring.get('password'),
                          connectionstring.get('database'))
        try:
            with con:
                cur = con.cursor()
                cur.execute(string)

            con.close()
            month.delete(0, END)
            day.delete(0, END)
            year.delete(0, END)
            vendor.delete(0, END)
            amt.delete(0,END)
            good = success()

        except:
            month.delete(0, END)
            day.delete(0, END)
            year.delete(0, END)
            vendor.delete(0, END)
            amt.delete(0, END)
            fail = error()


    submit = Button(window, text = "Save Invoice", command = pushit)
    submit.pack()