from tkinter import *
from tkinter.ttk import Combobox, Treeview
import pymysql as mdb
from Errordialog import *





def deleteinv():

    window = Tk()
    window.title("Delete inventory")

    recnumlbl = Label(window, text = "Record Num to Delete")
    recnumlbl.pack()

    recnum = Entry(window, width = 10)
    recnum.pack()

    def yes():
        #run delete DELETE FROM table_name WHERE condition;
        string = "DELETE from inventory where recordnum = " + str(recnum.get()) + ";"
        con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');
        try:
            with con:
                cur = con.cursor()
                cur.execute(string)

            con.close()
            recnum.delete(0, END)
            good = success()
            window.destroy()
        except:
            recnum.delete(0, END)
            fail = error()
            window.destroy()
        #success
    def no():
        recnum.delete(0,END)
        fail = error()
        window.destroy()
        #failure
        #clear fields

    def confirmdelete(result):
        window = Tk()
        window.title("Confirm Deletetion?")

        print(result)
        tree = Treeview(window, columns=('Record Num', 'Item ID', 'On Hand', 'Location'), show='headings')
        tree.heading('Record Num', text="Record Number")
        tree.heading('Item ID', text="Item ID")
        tree.heading('On Hand', text="On Hand")
        tree.heading('Location', text="Location")
        tree.insert("", "end", values=(result[0][0], result[0][1], result[0][2], result[0][3]))
        tree.pack()

        #yes button
        yesbtn = Button(window, text="Confirm", command=yes)
        yesbtn.pack()

        #no button
        nobtn = Button(window,text = "Cancel", command = no)
        nobtn.pack()


    def confirm():
        #get data
        query  = "Select * from inventory where recordnum =" + str(recnum.get()) + ";"

        con = mdb.connect('localhost', 'root', 'CSC436!', 'gameshop');

        with con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()
        con.close()

        confirmdelete(result)


        #delete on  yes, close the box on no and clear the rec num field.
    #submit button to fetch data and confirm that it's what you wanna delete
    # submit button
    submitbtn = Button(window, text="Submit", command=confirm)
    submitbtn.pack()


    #get data to delete


    #confirm deletion

    #delete


