
from tkinter import *
from tkinter.ttk import Combobox
import pymysql as mdb
from Errordialog import *
from python_mysql_dbconfig import read_db_config



def getdate():
    datewindow = Tk()
    datewindow.title("Enter Date")

    monthlbl = Label(datewindow, text="Month")
    monthlbl.pack()

    month = Combobox(datewindow)
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

    daylbl = Label(datewindow, text = "Day")
    daylbl.pack()

    daylist= []
    for i in range (1,31):
        daylist.append(str(i));
    day = Combobox(datewindow)
    day.pack()
    day['values']= daylist

    yearlbl = Label(datewindow, text= "Year")
    yearlbl.pack()
    yearlist = []
    for i in range(1990,2040):
        yearlist.append(str(i))
    year = Combobox(datewindow)
    year.pack()
    year['values'] = yearlist

    def processdates():
        #YYYY-MM-DD
        yeartp = year.get()
        monthtp = month.get()
        daytp = day.get()

        datestring = "'"+str(yeartp) +"-"+str(monthtp) + "-" + str(daytp)+"'"


    submit = Button(datewindow, text = "Submit", command = processdates)
    submit.pack()






def updateorder():
    #goal: update an order header shipdate or received date

    window = Tk()
    window.title("Update Header")

    orderIDlbl = Label(window, text = "OrderID")
    orderIDlbl.pack()
    orderid = Entry(window, width = 10)
    orderid.pack()

    def updateshipdate():
        datewindow = Tk()
        datewindow.title("Enter Date")

        monthlbl = Label(datewindow, text="Month")
        monthlbl.pack()

        month = Combobox(datewindow)
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

        daylbl = Label(datewindow, text="Day")
        daylbl.pack()

        daylist = []
        for i in range(1, 31):
            daylist.append(str(i));
        day = Combobox(datewindow)
        day.pack()
        day['values'] = daylist

        yearlbl = Label(datewindow, text="Year")
        yearlbl.pack()
        yearlist = []
        for i in range(1990, 2040):
            yearlist.append(str(i))
        year = Combobox(datewindow)
        year.pack()
        year['values'] = yearlist

        def processdates():
            # YYYY-MM-DD
            yeartp = year.get()
            monthtp = month.get()
            daytp = day.get()

            datestring = "'" + str(yeartp) + "-" + str(monthtp) + "-" + str(daytp) + "'"
            string = "Update orderheader set shipdate =" + datestring + " where orderID = " + "'"+str(orderid.get())+"';"

            con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');
            try:
                with con:
                    cur = con.cursor()
                    cur.execute(string)

                con.close()
                orderid.delete(0, END)
                datewindow.destroy()
                good = success()
            except:
                orderid.delete(0, END)
                fail = error()

        submit = Button(datewindow, text="Submit", command=processdates)
        submit.pack()

    shipdateupdate = Button(window, text = "Update Ship Date", command=updateshipdate)
    shipdateupdate.pack()

    def updaterecieved():
        datewindow = Tk()
        datewindow.title("Enter Date")

        monthlbl = Label(datewindow, text="Month")
        monthlbl.pack()

        month = Combobox(datewindow)
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

        daylbl = Label(datewindow, text="Day")
        daylbl.pack()

        daylist = []
        for i in range(1, 31):
            daylist.append(str(i));
        day = Combobox(datewindow)
        day.pack()
        day['values'] = daylist

        yearlbl = Label(datewindow, text="Year")
        yearlbl.pack()
        yearlist = []
        for i in range(1990, 2040):
            yearlist.append(str(i))
        year = Combobox(datewindow)
        year.pack()
        year['values'] = yearlist

        def processdates():
            # YYYY-MM-DD
            yeartp = year.get()
            monthtp = month.get()
            daytp = day.get()

            datestring = "'" + str(yeartp) + "-" + str(monthtp) + "-" + str(daytp) + "'"
            string = "Update orderheader set orderreceived =" + datestring + " where orderID = " + "'" + str(
                orderid.get()) + "';"

            connectionstring = read_db_config()
            con = mdb.connect(connectionstring.get('host'), connectionstring.get('user'),
                              connectionstring.get('password'),
                              connectionstring.get('database'))
            try:
                with con:
                    cur = con.cursor()
                    cur.execute(string)

                con.close()
                orderid.delete(0, END)
                datewindow.destroy()
                good = success()
            except:
                orderid.delete(0, END)
                fail = error()

        submit = Button(datewindow, text="Submit", command=processdates)
        submit.pack()

    recieveddate = Button(window, text= "Update Received Date", command =updaterecieved)
    recieveddate.pack()


