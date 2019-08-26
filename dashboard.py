import tkinter
import register
import attendence
import subprocess
import aboutus
import check_attendence

class Dashboard:
    def __init__(self):
        self.window = tkinter.Tk()
        self.init_tk()
        self.start()


    def init_tk(self):
        #self.window.iconbitmap('assets/AMS.ico')
        self.window.title("DASHBOARD")
        self.window.geometry('580x350')
        self.window.configure(background='snow')
        self.window.resizable(False, False)

        self.registerBtn = tkinter.Button(self.window, text="Register student", command=self.registerBtn, fg="white",bg="#4A7164", width=50, height=2,activebackground = "Red", font = ('times', 15, ' bold '))
        self.registerBtn.place(x=0, y=0)



        self.BrowseBtn = tkinter.Button(self.window, text="Database Entry", command=self.BrowseBtn, fg="white",
                                        bg="#4A7164", width=50, height=2, activebackground="Red",
                                        font=('times', 15, ' bold '))
        self.BrowseBtn.place(x=0, y=180)


        self.CheckBtn = tkinter.Button(self.window, text="Check Attendance", command=self.checkAttendence, fg="white",
                                        bg="#4A7164", width=50, height=2, activebackground="Red",
                                        font=('times', 15, ' bold '))
        self.CheckBtn.place(x=0, y=122)


        self.attendenceBtn = tkinter.Button(self.window, text="Automatic Attendance", command=self.attendenceBtn, fg="white",
                                          bg="#4A7164", width=50, height=2, activebackground="Red",
                                          font=('times', 15, ' bold '))
        self.attendenceBtn.place(x=0, y=60)

        self.aboutBtn = tkinter.Button(self.window, text="About Us", command=self.aboutUs, fg="white",
                                          bg="#4A7164", width=50, height=2, activebackground="Red",
                                          font=('times', 15, ' bold '))
        self.aboutBtn.place(x=0, y=237)

        self.manualBtn = tkinter.Button(self.window, text="Exit", command=self.exitCall, fg="white",
                                          bg="#4A7164", width=50, height=2, activebackground="Red",
                                          font=('times', 15, ' bold '))
        self.manualBtn.place(x=0, y=294)



    def start(self):
        self.window.mainloop()

    def BrowseBtn(self):
        subprocess.run(["db_browser/db.exe", "attendence.db"])
        pass

    def aboutUs(self):
        about = aboutus.Aboutus()
        about.start()


    def exitCall(self):
        print("GOOD BYE")
        exit(0)



    def registerBtn(self):
        print("clicked")
        r = register.Register()
        r.start()

    def attendenceBtn(self):
        att = attendence.Attendence()
        att.start()

    def checkAttendence(self):
        catt = check_attendence.CheckAttendence()
        catt.start()
