import sqlite3
import time
from dateutil import parser

conn = sqlite3.connect('attendence.db')
#conn = sqlite3.connect('C:\\Users\\JEEONE\\Documents\\code\\attendence\\attendence.db')

SUBDATA = {
    "1":("IT", "CALCLUS", " C PROGRAMMING"),
    "2":("DIGITAL LOGIC", "STAT II"),
    "3":("OS", "NM"),
    "4":("TOC", "COGNITIVE SCIENCE"),
    "5":("E GOVERNANCE", "COMPUTER NETWORK"),
    "6":("COMPILER", "RTS"),
    "7":("JAVA", "SPM"),
    "8":("CLOUD COMPUTING", "DATA WAREHOUSE AND DATA MINING")
}

def getSubjectBySem(sem):
    return SUBDATA[sem]

def isSemisterValid(sem):
    if sem in SUBDATA:
        return True
    return  False


def isSubjectValid(sem, sub):
    if sem in SUBDATA:
        if sub in SUBDATA[sem]:
            return True

    return  False


def initDb():

    c = conn.cursor()
    try:
        #create students table
        for sem in SUBDATA:
            query = 'CREATE TABLE {} (id integer primary key, name text, etytime text, semester text)'.format("student_"+sem)
            c.execute(query)

        # create attendence table
        for sem in SUBDATA:
            query = 'CREATE TABLE {} ( attendtime text primary key, id integer, name text, subject text)'.format("attend_" + sem)
            c.execute(query)
        conn.commit()
    except Exception as e:
        pass
    #registerAttendance(10.9, 1, "com", "2")
    #registerStudent(1, "good", 10.6, "2")
    #registerStudent(8, "asas", 10.6, "2")
    #registerStudent(3, "xaax", 10.6, "2")
    #print(getHighestId("2"))
    #print(getHighestId("1"))
    #print(getAttendendenceData("2"))
    checkAttendence2("7")

def registerStudent(id, name, etime, sem):
    query = 'INSERT INTO {} VALUES (?,?,?,?)'.format("student_"+sem)
    print(query)
    try:
        c = conn.cursor()
        c.executemany(query, [(id, name, etime, sem)])
        conn.commit()
    except Exception as e:
        print(e)

def registerAttendance(attendtime, id, name,subject,semester):
    query = 'INSERT INTO {} VALUES (?,?,?,?)'.format("attend_"+semester)
    print(query)
    try:
        c = conn.cursor()
        c.executemany(query, [(attendtime, id,name, subject)])
        conn.commit()
    except Exception as e:
        print(e)

def getNameFromId(id, sem):
    c = conn.cursor()
    query = 'SELECT name FROM {} WHERE id={}'.format("student_"+sem, id)
    response = c.execute(query)

    try:
        return response.fetchone()[0]
    except Exception as e:
        print(e)
        return "Not in DB"

def getHighestId(sem):
    c = conn.cursor()
    query = 'SELECT id FROM {}  ORDER BY id DESC LIMIT 1'.format("student_" + sem)
    print(query)
    response = c.execute(query)
    try:
        return response.fetchone()[0]
    except Exception as e:
        print(e)
        return 0


def getAttendendenceData(sem):
    c = conn.cursor()
    query = 'SELECT attendtime, id, name, subject FROM {}'.format("attend_" + sem)
    response = c.execute(query)

    alldata = []

    try:
        for row in response:
            currentData = {}
            currentData["attendtime"] = row[0]
            currentData["id"] = row[1]
            currentData["name"] = row[2]
            currentData["subject"] = row[3]
            alldata.append(currentData)

    except Exception as e:
        return alldata
    return alldata

def getAllRegisteredStudents(sem):
    c = conn.cursor()
    query = 'SELECT  id, name FROM {}'.format("student_" + sem)
    response = c.execute(query)

    alldata = []

    try:
        #print(response)
        for row in response:
            currentData = {}
            currentData["id"] = row[0]
            currentData["name"] = row[1]
            print(currentData)
            alldata.append(currentData)

    except Exception as e:
        return alldata
    return alldata



def checkAttendence(sem):
    allAttendence = getAttendendenceData(sem)
    #print(allAttendence)
    print("jdusduduedueuuu")
    attendence_processed = {}
    attendableDate = []

    for attndence in allAttendence:

        #print(attndence)
        dt = parser.parse(attndence['attendtime'])
        #print(dir(dt))
        day = str(dt.day)
        month = str(dt.month)
        year = str(dt.year)
        key = "{}_{}_{}_{}_{}_{}".format(year,day,month,sem,str(attndence['id']),attndence['subject'])

        attdate = "{}_{}_{}".format(year,day,month)
        if attdate not in attendableDate:
            attendableDate.append(attdate)
        attendence_processed[key] = True

    #print(attendence_processed)
    #print(attendableDate)
    allRegisteredstd = getAllRegisteredStudents(sem)

    #print(allRegisteredstd)

    allRegisteredStdProcessed = {}

    for day in attendableDate:
        for regstd in allRegisteredstd:
            #print(regstd)
            for subj in SUBDATA[sem]:
                print(subj)
                key = "{}_{}_{}_{}".format(day, sem, str(regstd['id']), subj)
                print(key)
                allRegisteredStdProcessed[key] = {
                "day":day,
                "name":regstd['name'],
                "sem":sem,
                "subject":subj,
                "present":False
            }
    for key in attendence_processed.keys():
        info = allRegisteredStdProcessed[key]
        info["present"] = True

    print(allRegisteredStdProcessed)


def checkAttendence2(sem):
    allAttendence = getAttendendenceData(sem)
    #print(allAttendence)
    print("jdusduduedueuuu")
    attendence_processed = {}
    attendableDate = []

    for attndence in allAttendence:

        #print(attndence)
        dt = parser.parse(attndence['attendtime'])
        #print(dir(dt))
        day = str(dt.day)
        month = str(dt.month)
        year = str(dt.year)
        key = "{}_{}_{}_{}_{}_{}".format(year,day,month,sem,str(attndence['id']),attndence['subject'])

        attdate = "{}_{}_{}".format(year,day,month)
        if attdate not in attendableDate:
            attendableDate.append(attdate)
        attendence_processed[key] = True

    #print(attendence_processed)
    #print(attendableDate)
    allRegisteredstd = getAllRegisteredStudents(sem)

    #print(allRegisteredstd)

    allRegisteredStdProcessed = {}

    for day in attendableDate:
        for regstd in allRegisteredstd:
            #print(regstd)
            for subj in SUBDATA[sem]:
                print(subj)
                key = "{}_{}_{}_{}".format(day, sem, str(regstd['id']), subj)
                print(key)
                allRegisteredStdProcessed[key] = {
                "day":day,
                "name":regstd['name'],
                "sem":sem,
                "subject":subj,
                "present":False
            }
    for key in attendence_processed.keys():
        info = allRegisteredStdProcessed[key]
        info["present"] = True

    return allRegisteredStdProcessed

