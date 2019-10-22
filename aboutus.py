import tkinter
import database


class Aboutus:
    def __init__(self):
        self.window = tkinter.Tk()
        self.data = database.getAttendendenceData("2")
        self.window.geometry('400x2500')
        self.init_tk()
        self.window.resizable(False, False)


    def init_tk(self):
        self.window.iconbitmap('assets/AMS.ico')
        self.window.title("About Us")
        self.window.geometry('580x320')
        self.window.configure(background='snow')

        lbl = tkinter.Label(self.window, text="About Us description",  background="snow", font=('times', 25, ' bold '))

        #lbl.grid(column=0, row=1)
        lbl.place(x=250, y=10)

        #whatever_you_do = "Whatever you do will be insignificant nvfknkf fljlfkfgj gjflfj fdlkjdlf lfkjdlkfd , but it is very important that you do it.\n(Mahatma Gandhi)"
        #msg = tkinter.Message(self.window, text=whatever_you_do)
        #msg.config(bg='lightgreen', font=('times', 15, 'italic') , width=585)
        #msg.grid(column=0, row=2)
        #msg.pack(side=tkinter.RIGHT)

        About_us = "fjdhjdf rfjjfhj fjfjfrj rfjfrjf fkjjfkjr rfjfrjkf fjjkjnrkjfl rfjrfrkjfn fjnk \njnkdjj fjdkjnk djnkjf djdk"
        lbl = tkinter.Label(self.window, text=Aboutt_us, background="lightgreen", font=('times', 15, ' italic '))

        # lbl.grid(column=0, row=1)
        lbl.place(x=10, y=80)



        #lbl = tkinter.Label(self.window, text="\nWe the students of indreni college did a project on smart attendance using facial biometrics.nkdkjndkjsd dnkjdnkj dfkjdnfkjdnfk dkndkjnk mcnmnc\n cxmcmxcm cmxcmxc xn cxmcxcmx cmnxcx mcn cmxcmxcmx  cxcmnx cm    SThis project\n is based on face detection and recognitiondbjbdjbsdjsbbkds kjdfkjdf fjjdfnkjdfkd fkjndkjdfn fjndfkjd fjdfdjkfd dkfndkjfjndkfkdfndkfndk  fkdfndkfndk fkdnfkdfnn fndkfndk \n sh", background="snow", font=('times', 10, ' bold '))
        #lbl.place(x=0, y=50)

        #T = tkinter.Text(self.window, height=2, width=30)
        #T.place(x=0,y=200)
        #T.pack()
        #T.insert(tkinter.END, "Just a text Widget\nin two lines\n")

        #ADD LABELS

        #self.registerBtn = tkinter.Button(self.window, text="Register student", command=self.registerBtn, fg="white",bg="deep pink", width=20, height=2,activebackground = "Red", font = ('times', 15, ' bold '))
        #self.registerBtn.place(x=0, y=0)



    def start(self):
        self.window.mainloop()

