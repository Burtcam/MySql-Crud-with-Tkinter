from tkinter import *

class error():
    def __init__(self):
        self.root = Tk()
        label = Label(self.root, text = "Error!, Data not saved")
        label.pack()
        button = Button(self.root, text = 'Close', command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()


class success():
    def __init__(self):
        self.root = Tk()
        label = Label(self.root, text="Success! Data Saved to Database")
        label.pack()
        button = Button(self.root, text='Close', command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()



