import tkinter
import database

class Browse:
    def __init__(self):
        self.window = tkinter.Tk()
        self.data = database.getAttendendenceData("2")
        self.init_tk()


    def init_tk(self):
        self.window.iconbitmap('assets/AMS.ico')
        self.window.title("Browse Data")
        self.window.geometry('580x320')
        self.window.configure(background='snow')

        self.registerBtn = tkinter.Button(self.window, text="Register student", command=self.registerBtn, fg="white",bg="deep pink", width=20, height=2,activebackground = "Red", font = ('times', 15, ' bold '))
        self.registerBtn.place(x=0, y=0)



    def start(self):
        self.window.mainloop()