from tkinter import *
from threading import Timer


def Notify(s):
    popupRoot = Tk()
    popupRoot.overrideredirect(1)
    popupRoot.after(2000, popupRoot.destroy)
    popupButton = Button(popupRoot, text = s, font = ("Verdana", 12), bg = "yellow", command = popupRoot.destroy)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()




def Notify2(window,s):
    popupButton = Button(window, text=s, font=("Verdana", 12), bg="yellow", command=lambda:popupButton.pack_forget())
    popupButton.pack()


def Notify3(window,s):
    mylabel = Label(window, text=s, font=("Verdana", 12), bg="red")


    def timeout():
        mylabel.pack_forget()

    t = Timer(3, timeout)
    t.start()
    mylabel.place(x=30,y=40)
    mylabel.pack()


def Notifybadass(window,s):
    mylabel = Label(window, text=s, font=("Verdana", 12), bg="green")
    mylabel.place(x=10,y=20)

    def timeout():
        mylabel.pack_forget()
        window.destroy()
    t = Timer(3, timeout)
    t.start()
    mylabel.pack()


import tkinter as tk
# import Tkinter as tk # for Python 2.X


class MessageWindow(tk.Toplevel):
    def __init__(self, title, message):
        super().__init__()
        self.details_expanded = False
        self.title(title)
        self.geometry("300x75+{}+{}".format(self.master.winfo_x(), self.master.winfo_y()))
        self.resizable(False, False)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        tk.Label(self, text=message).grid(row=0, column=0, columnspan=3, pady=(7, 7), padx=(7, 7), sticky="ew")

        tk.Button(self, text="OK", command=self.master.destroy).grid(row=1, column=1, sticky="e")
        tk.Button(self, text="Cancel", command=self.destroy).grid(row=1, column=2, padx=(7, 7), sticky="e")


def exit_root():
    MessageWindow("Quit", "Are you sure you want to quit?")



