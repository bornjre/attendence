import tkinter
import noti
from tkinter import messagebox


class Admin:
    def __init__(self):
        self.window = tkinter.Tk()
        self.init_tk()
        self.window.title("Admin")
        self.window.geometry('1280x720')
        self.verified = False

    def init_tk(self):
        print("@inside admin")

        self.C = tkinter.Canvas(self.window, bg="blue", height=1600, width=1080)
        #self.filename = tkinter.PhotoImage(file="C:\\Users\\JEEONE\\Desktop\\face33.png")
        #self.background_label = tkinter.Label(self.window, image=self.filename)
        #self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #self.Noti = tkinter.Label(self.window, text="Enter password", bg="Green", fg="white", width=15,height=3, font=('times', 17, 'bold'))
        #self.Noti.place(x=0, y=0)
        #def Noticlear():
        #    pass


        self.loginBtn = tkinter.Button(self.window, text="Login", command=self.loginClick, fg="white",
                                        bg="#737973", width=5, height=1, activebackground="Red",
                                        font=('times', 13, ' bold '))
        self.loginBtn.place(x=1060, y=300)

        self.namelbl = tkinter.Label(self.window, text="Username", width=15, height=1, fg="white", bg="#5C8E5A",
                       font=('times', 15, ' bold '))
        self.namelbl.place(x=900, y=200)
        #style.configure('ENR', borderwidth='4')

        self.userInput = tkinter.Entry(self.window, width=17, validate='key', bg="#637C62", fg="black", font=('times', 16, ' bold '))
        self.userInput.place(x=1100, y=200)

        self.namelbl = tkinter.Label(self.window, text="Password", width=15, height=1, fg="white", bg="#5C8E5A",
                                     font=('times', 15, ' bold '))
        self.namelbl.place(x=900, y=250)
        self.passInput = tkinter.Entry(self.window, width=17, validate='key', show="*", bg="#637C62", fg="black", font=('times', 16, ' bold '))
        self.passInput.place(x=1100, y=250)

        #self.window.iconbitmap('assets/AMS.ico')
        self.window.title("")
        self.window.geometry('1280x900')
        self.window.configure(background='snow')

    def start(self):

        self.C.pack()
        self.window.mainloop()
        return self.verified


    def loginClick(self):
        self.user = self.userInput.get()
        self._pass = self.passInput.get()
        if self.user != "123" or self._pass != "123":
            print("Invalid login details")


            messagebox.showwarning('WARNING', 'INVALID USERRNAME OR PASSWORD!!!')
            #noti.Notify3(self.window, "invalid password")
            print("invalid semister")
            return
        self.verified = True
        self.window.destroy()