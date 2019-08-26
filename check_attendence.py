import tkinter
import noti
import csv
import database
import subprocess
import os
from tkinter import messagebox

class CheckAttendence:
    def __init__(self, db=[]):
        self.database = db
        self.window = tkinter.Tk()
        self.Selected_Sem = "0"
        self.Subject = ""
        self.fakelist = {}
        self.init_tk()
        self.window.resizable(False, False)

    def init_tk(self):
        print("Attendence!!")
        self.window.iconbitmap('assets/AMS.ico')
        self.window.title("Attendence")
        self.window.geometry('460x250')
        self.window.configure(background='#B2ACAC')



        self.NextBtn = tkinter.Button(self.window, text="check", command=self.nextClick, fg="white",
                                        bg="#737973", width=5, height=1, activebackground="Red",
                                        font=('times', 13, ' bold '))
        self.NextBtn.place(x=170, y=150)




        self.namelbl = tkinter.Label(self.window, text="Enter semester", width=15, height=1, fg="white", bg="#5C8E5A",
                                     font=('times', 15, ' bold '))
        self.namelbl.place(x=10, y=50)
        self.semInput = tkinter.Entry(self.window, width=20, validate='key', bg="#637C62", fg="black", font=('times', 16, ' bold '))
        self.semInput.place(x=220, y=50)

        self.namelbl = tkinter.Label(self.window, text="Enter subject", width=15, height=1, fg="white", bg="#5C8E5A",
                                     font=('times', 15, ' bold '))
        self.namelbl.place(x=10, y=100)
        self.subInput = tkinter.Entry(self.window, width=20, validate='key', bg="#637C62", fg="black", font=('times', 16, ' bold '))
        self.subInput.place(x=220, y=100)



    def start(self):
        self.window.mainloop()

    def nextClick(self):
        print("clicked")
        self.Selected_Sem = self.semInput.get()
        self.Subject = self.subInput.get().upper()


        if not database.isSemisterValid(self.Selected_Sem):
            messagebox.showwarning('WARNING', 'Please enter the valid semester!!!')
            #noti.Notify3(self.window,"Invalid Semester")
            print("invalid semister")
            return

        if not database.isSubjectValid(self.Selected_Sem,self.Subject):
            messagebox.showwarning('WARNING', 'Please enter the valid subject!!!')
            #noti.Notify3(self.window, "Invalid Subject")
            print("invalid subject")
            return

        self.csv_writer()

        #TODO open that self.Subject in explorer


    def csv_writer(self):
        stub_data = database.checkAttendence2(self.Selected_Sem)

        csvwriters = {}
        csvFilenames = {}
        sem = self.Selected_Sem
        subjects = database.SUBDATA[sem]
        for sub in subjects:
            filename = "modeldata\\attendence_csv\\attendence_{}_{}.csv".format(sem, sub)
            csvFilenames[sub] = filename
            ofile = open(filename, 'w', newline='')
            csvwriters[sub] = csv.writer(ofile)
        title = False
        row = 1
        lastkeys = {}
        for key, value in stub_data.items():
            sub3 = value["subject"]
            del value["subject"]
            print("here")
            print(sub3)

            datekey = value["day"]

            if not title:
                title = True
                for sub2 in subjects:
                    _writer =  csvwriters[sub2]
                    _writer.writerow(value.keys())
                #print(value.keys())

            _writer = csvwriters[sub3]
            if sub3 in lastkeys and ( lastkeys[sub3] != datekey):
                print("not equal", lastkeys[sub3]," ", datekey)
                _writer.writerow([])
            _writer.writerow(value.values())
            lastkeys[sub3] = datekey
            #print(key)
            row+=1

        #print(csvFilenames[self.Subject])
        #subprocess.run(['open', csvFilenames[self.Subject]], check=True)
        os.startfile(csvFilenames[self.Subject])
        #subprocess.check_call(['open', csvFilenames[self.Subject]])