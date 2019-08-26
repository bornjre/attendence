import tkinter
import cv2
import utils
import numpy as np
import config
import database
import time
import noti
import os
from tkinter import messagebox
from threading import Timer

import subprocess

class Register:
    def __init__(self, db=[]):
        self.database = db
        self.window = tkinter.Tk()
        self.Selected_name = ""
        self.Selected_Sem = ""
        self.init_tk()
        self.detector = {}
        self.thisid = 0
        self.window.resizable(False, False)

    def init_tk(self):
        print("@inside register___@@@")
        #self.window.iconbitmap('assets/AMS.ico')
        self.window.title("Student Register")
        self.window.geometry('450x250')
        self.window.configure(background='#B2ACAC')



        self.NextBtn = tkinter.Button(self.window, text="Next", command=self.nextClick, fg="white",
                                        bg="#737973", width=5, height=1, activebackground="Red",
                                        font=('times', 13, ' bold '))
        self.NextBtn.place(x=280, y=150)

        self.ClearBtn = tkinter.Button(self.window, text="Clear", command=self.clearClick, fg="white",
                                      bg="#737973", width=5, height=1, activebackground="Red",
                                      font=('times', 13, ' bold '))
        self.ClearBtn.place(x=350, y=150)

        self.namelbl = tkinter.Label(self.window, text="Enter semester", width=15, height=1, fg="white", bg="#5C8E5A",
                                     font=('times', 15, ' bold '))
        self.namelbl.place(x=10, y=50)
        self.semInput = tkinter.Entry(self.window, width=17, validate='key', bg="#637C62", fg="black", font=('times', 16, ' bold '))
        self.semInput.place(x=220, y=50)
        self.namelbl = tkinter.Label(self.window, text="Enter name", width=15, height=1, fg="white", bg="#5C8E5A",
                                     font=('times', 15, ' bold '))
        self.namelbl.place(x=10, y=100)
        self.nameInput = tkinter.Entry(self.window, width=17, validate='key', bg="#637C62", fg="black", font=('times', 16, ' bold '))
        self.nameInput.place(x=220, y=100)

    def start(self):

        self.window.mainloop()
    def clearClick(self):

        self.semInput.delete(first=0,last=22)
        self.nameInput.delete(first=0,last=22)


    def nextClick(self):


        self.Selected_Sem = self.semInput.get()
        self.Selected_name = self.nameInput.get()
        if not(self.Selected_name):

            #messagebox.showwarning('WARNING','Please enter the required fields!!!')
            noti.MessageWindow("Quit ", "Enter the bdbdhe?")
            #=Button(self.window, text='ok', command='nextClicked')


            #noti.Notify3(self.window, "Fill required fields!!!")
            print("fill necessary fields")
            return

        if not database.isSemisterValid(self.Selected_Sem):
            messagebox.showwarning('WARNING', 'Please enter the valid semester!!!')
            #noti.Notify3(self.window, "Fill valid semester!!!")
            print("fill necessary fields")
            #print("semester does not exist")
            print(type(self.Selected_Sem))
            print(self.Selected_Sem)

            return

        self.getImages()
        self.train_tf(self.Selected_Sem)
        self.finish()

    def getImages(self):
        cam = cv2.VideoCapture(0)
        self.detector = cv2.CascadeClassifier(config.HARFILED)
        self.thisid = database.getHighestId(self.Selected_Sem) + 1
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder
                #cv2.imwrite( config.getSemImagePath(self.Selected_Sem) + self.Selected_name + "." + str(self.thisid) + '.' + str(
                #    sampleNum) + ".jpg",
                #            gray[y:y + h, x:x + w])

                imgdir = config.getSemImagePathtf(self.Selected_Sem) + str(self.thisid)
                if not os.path.exists(imgdir):
                    os.makedirs(imgdir)

                print(imgdir)

                cv2.imwrite( imgdir + "/"
                     + self.Selected_name + "." + str(self.thisid) + '.' + str(
                        sampleNum) + ".jpg",
                    img[y:y + h, x:x + w])
                cv2.imshow('Frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 200:
                break
        cam.release()
        cv2.destroyAllWindows()

    def train_tf(self, semfolder):
        path = "modeldata/tf_train/{}".format(semfolder)
        folder = "--image_dir={}".format(path)
        subprocess.call(['python', 'modeldata/tf_train/retrain.py',
                         folder,
                         "--output_graph={}/trained_graph.pb".format(path), "--output_labels={}/mylabels.txt".format(path) ])

    #
    # def trainImages(self):
    #     recognizer = cv2.face.LBPHFaceRecognizer_create()
    #
    #     faces = []
    #     Id = []
    #     self.detector = cv2.CascadeClassifier(config.HARFILED)
    #     path = "modeldata\\image\\" + self.Selected_Sem
    #     #print(os.listdir(path))
    #     print(path)
    #     try:
    #         faces, Id = utils.getImagesAndLabels(path, self.detector)
    #     except Exception as e:
    #         print(e)
    #         print('please make TrainingImage folder & put Images')
    #
    #     recognizer.train(faces, np.array(Id))
    #     try:
    #
    #         recognizer.save(config.getTrainedModelPath(self.Selected_Sem))
    #     except Exception as e:
    #         print("folder not found!")


    def finish(self):
        database.registerStudent(self.thisid,self.Selected_name,  time.asctime(time.localtime(time.time())),self.Selected_Sem )
        print("Registering", self.thisid,self.Selected_name,self.Selected_Sem)
        #noti.Notify3(self.window, "invalid password")
        #self.window.destroy()

        global notifica
        notifica = tkinter.Label(self.window, text="Model trained and successfully registred", bg="lightgreen", fg="white",
                                 width=30,
                                 height=1, font=("Verdana", 9))
        M = 'Model trained and successfully registred'
        notifica.configure(text=M, bg="lightgreen", fg="black", width=30, font=('times', 15, 'bold'))
        notifica.place(x=50, y=200)

        def timeout():
            notifica.pack_forget()
            notifica.destroy()

        t = Timer(3, timeout)
        t.start()



        #noti.Notifybadass(self.window, "Model trained and successfully registred")