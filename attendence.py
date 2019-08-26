import tkinter
from tkinter import ttk
import time
import config
import cv2
import database
import noti
from tkinter import messagebox
from threading import Timer
import classify
from keras.preprocessing import image
import  numpy as np
import threading

class Attendence:
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
        #self.window.iconbitmap('assets/AMS.ico')
        self.window.title("Attendence")
        self.window.geometry('460x250')
        self.window.configure(background='#B2ACAC')



        self.NextBtn = tkinter.Button(self.window, text="Next", command=self.nextClick, fg="white",
                                        bg="#737973", width=5, height=1, activebackground="Red",
                                        font=('times', 13, ' bold '))
        self.NextBtn.place(x=170, y=200)

        
        self.CheckSub = tkinter.Button(self.window, text="CheckSub", command=self.checkSubFunc, fg="white",
                                        bg="#737973", width=5, height=1, activebackground="Red",
                                        font=('times', 13, ' bold '))
        self.CheckSub.place(x=250, y=20)

        self.namelbl = tkinter.Label(self.window, text="Enter semester", width=15, height=1, fg="white", bg="#5C8E5A",
                                     font=('times', 15, ' bold '))
        self.namelbl.place(x=10, y=50)
        self.semInput = tkinter.Entry(self.window, width=20, validate='key', bg="#637C62", fg="black", font=('times', 16, ' bold '))
        self.semInput.place(x=220, y=50)

        self.namelbl = tkinter.Label(self.window, text="Choose subject", width=15, height=1, fg="white", bg="#5C8E5A",
                                     font=('times', 15, ' bold '))
        self.namelbl.place(x=10, y=100)
        #self.subInput = tkinter.Entry(self.window, width=20, validate='key', bg="#637C62", fg="black", font=('times', 16, ' bold '))
        #self.subInput.place(x=220, y=100)
        


    def checkSubFunc(self):
        self.Selected_Sem = self.semInput.get()
        subjs = database.getSubjectBySem(self.Selected_Sem)
        self.listbox = ttk.Combobox(self.window, values=subjs)
        self.listbox.place(x=170, y=50)
        self.listbox.pack()


    def start(self):
        self.window.mainloop()

    def nextClick(self):
        print("clicked")
        self.Selected_Sem = self.semInput.get()
        #self.Subject = self.subInput.get().upper()
        self.Subject = self.listbox.get()


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

        self.Attedence()

    def Attedence(self):
        now = time.time()  ###For calculate seconds of video
        future = now + 20


        #recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        #try:
        #    recognizer.read(config.getTrainedModelPath(self.Selected_Sem))
        #except Exception as e:
        #    print(e)
        faceCascade = cv2.CascadeClassifier(config.HARFILED);

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        detectedList = {}

        path = "modeldata/tf_train/{}".format(self.Selected_Sem)
        tfclassfier = classify.Classifier(path)

        inChanel = []
        outChanel = []

        thread = threading.Thread(target=tfclassfier.run_loop, args=(inChanel, outChanel))
        thread.start()
        count = 0
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            #print(type(faces))
            for (x, y, w, h) in faces:

                #Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

                detected_face = im[int(y):int(y + h), int(x):int(x + w)]  # crop detected face
                #detected_face = cv2.resize(detected_face, (299, 299))  # resize to 48x48
                detected_face = cv2.resize(detected_face, (224, 224))

                img_pixels = image.img_to_array(detected_face)
                img_pixels = np.expand_dims(img_pixels, axis=0)

                img_pixels /= 255  # pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1


                #Id, conf = tfclassfier.run(img_pixels)
                print("shape of processed nparray :",img_pixels.shape)
                print("shape of faces nparray :",faces.shape)
                inChanel.append((count, img_pixels))
                Id = None
                conf = None
                detection = True

                try:
                    o = outChanel.pop()
                    Id = o[0]
                    conf = o[1]      
                except IndexError:
                    detection = False
                    pass

                if conf and (conf > 0.8) :
                    idname = database.getNameFromId(Id, self.Selected_Sem)
                    if not idname == "Not in DB":
                        detectedList[Id] = idname

                    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                    cv2.putText(im, idname + " " + str(conf), (x + h, y), font, 1, (255, 255, 0,), 4)
                

                else:
                    tt = 'Unknown'
                    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                    cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
            if time.time() > future:
                break
            count += 1

            #attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
            cv2.imshow('Filling attedance..', im)
            key = cv2.waitKey(30) & 0xff
            if key == 27:
                break
        cam.release()
        cv2.destroyAllWindows()
        #now save to db


        for key in detectedList:

            localtime = time.asctime(time.localtime(time.time()))
            name = detectedList[key]
            database.registerAttendance(localtime,key, name,self.Subject,self.Selected_Sem )
            time.sleep( 1 )

        print(detectedList)
        global notifica
        notifica = tkinter.Label(self.window, text="Attendance filled Successfully", bg="lightgreen", fg="white", width=20,
                            height=1, font=("Verdana", 9))
        M = 'Attendance filled Successfully'
        notifica.configure(text=M, bg="lightgreen", fg="black", width=22, font=('times', 15, 'bold'))
        notifica.place(x=100, y=200)

        def timeout():
            notifica.pack_forget()
            self.window.destroy()

        t = Timer(3, timeout)
        t.start()

        #noti.Notifybadass(self.window, "Attendance Successfull")
