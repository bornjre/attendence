import tkinter
import csv


class Browser:
    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Browse attendence")
        self.window.geometry('1280x720')
        self.stub_data = {'2019_11_8_7_1_JAVA': {'day': '2019_11_8', 'name': 'JAVA', 'sem': '7', 'subject': 'JAVA', 'present': True}, '2019_11_8_7_1_SPM': {'day': '2019_11_8', 'name': 'JAVA', 'sem': '7', 'subject': 'SPM', 'present': False}, '2019_11_8_7_2_JAVA': {'day': '2019_11_8', 'name': 'jeon', 'sem': '7', 'subject': 'JAVA', 'present': True}, '2019_11_8_7_2_SPM': {'day': '2019_11_8', 'name': 'jeon', 'sem': '7', 'subject': 'SPM', 'present': False}}
        self.init_tk()

    def init_tk(self):
        print("attendence")
        #testrow = self.stub_data[self.stub_data.keys()[0]]
        #for titlenames in testrow.keys():
        #    print(titlenames)


        title = False
        row = 1
        for key, value in self.stub_data.items():
            if not title:
                title = True
                col = 0
                print(value.keys())
                for key2 in value.keys():
                    print(key2)
                    b = tkinter.Label(self.window, text=key2, fg="#000")
                    b.grid(row=0, column=col)
                    col +=1
            col=0
            print(value.values())
            for v in value.values():
                b = tkinter.Label(self.window, text=v, fg="#000")
                b.grid(row=row, column=col)
                col+=1
            row+=1

        self.csv_writer()
        #csvFile.close()

    def csv_writer(self):
        csvwriters = {}
        #csvFilenames = {}
        sem = "7"
        subjects = ("JAVA", "SPM")
        for sub in subjects:
            filename = "modeldata\\attendence_csv\\attendence_{}_{}.csv".format(sem, sub)
            #csvFilenames[sub] = filename
            ofile = open(filename, 'w', newline='')
            csvwriters[sub] = csv.writer(ofile)
        title = False
        row = 1
        for key, value in self.stub_data.items():
            sub3 = value["subject"]
            del value["subject"]

            if not title:
                title = True
                for sub2 in subjects:
                    _writer =  csvwriters[sub2]
                    _writer.writerow(value.keys())
                print(value.keys())

            _writer = csvwriters[sub3]
            _writer.writerow(value.values())
            row+=1



    def start(self):
        self.window.mainloop()

b = Browser()
b.start()