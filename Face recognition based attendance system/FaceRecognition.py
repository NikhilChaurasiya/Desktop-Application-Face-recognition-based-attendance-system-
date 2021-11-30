import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import cv2, os
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
from time import strftime
import tkinter.ttk as ttk
from tkinter.constants import *
import openpyxl
import re

window = tk.Tk()
window.title("Face Recognition")
window.geometry('1366x768+0+0')
dialog_title = 'QUIT'
dialog_text = 'Are you Sure?'
# window.overrideredirect(1)
window.attributes('-fullscreen', True)
# window.resizable(0,0)
# window.configure(background='orange')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# -----------------------THIS IS FOR BACKGROUND IMAGE-----------------------------


# -------------------------------------USER INPUTS--------------------------------

message = tk.Label(window, text="MAKES YOUR ATTENDANCE EASY", fg="#ffffff", bg="#262626", width=60,height=2,
                   font=('Magical Stylish Sans Serif Demo', 35))
message.config(anchor=CENTER)
message.pack()

'''---------------------------------------------CLOCK-------------------------------------------------------------'''


def time1():
    string = strftime('%B %d ,%Y | %H :%M :%S %p')
    lbl3.config(text=string)
    lbl3.after(1000, time1)


lbl3 = Label(window, font=('calibri', 16), background='#262626', foreground='white', height=1, width=142)
lbl3.config(anchor=CENTER)
lbl3.pack()
time1()

canvas = Canvas(window, width=1600, height=900)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(
    "iconImages\\glow-white-gradient-hexagon-black-1920x1080-c4-ffffff-ffffff-fffff0-000000-l2-1-27-a-10-f-6.png"))
canvas.create_image(730, 0, anchor=N, image=img)
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
main_frame = LabelFrame(window, text="", borderwidth=5, relief="groove")
main_frame.place(x=105, y=180, height=310, width=745)

main_frame_att = LabelFrame(window, text="", borderwidth=5, relief="groove")
main_frame_att.place(x=105, y=485, height=286, width=745)

manage_frame = LabelFrame(window, text="", borderwidth=5, relief="groove", bg="white")
manage_frame.place(y=175, x=870, height=495, width=480)
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
head = tk.Label(window, text=" REGISTER HERE ONLY ONCE TO SAVE YOUR IMAGE IN DATABASE ",
                font=("Magical Stylish Sans Serif Demo", 16), bg="#383838", fg="white")
head.config(anchor=CENTER)
head.place(x=105, y=180, height=48, width=743)

lbl = tk.Label(window, text="ID", width=12, height=1, fg='white', bg="#808080", font=('consolas', 19))
lbl.place(x=120, y=255)
txt = tk.Entry(window, width=30, bg="#ffffff", fg="black", font=('consolas', 22))
txt.place(x=293, y=255)

lbl2 = tk.Label(window, text="BRANCH", width=13, height=1, fg='white', bg="#808080", font=('consolas', 19))
lbl2.place(x=120, y=308)
txt2 = tk.Entry(window, width=30, bg="#ffffff", fg="black", font=('arial', 22))
txt2.place(x=293, y=308)

# lbl3=tk.Label(window,text="NOTIFICATION", width=20,height=2,fg='orange', font=('OCR A Extended',20,'bold'))
# lbl3.place(x=300,y=365)

imglogo = ImageTk.PhotoImage(file="iconImages/favicon (3).ico")
imglogo1 = Label(window, image=imglogo, bg="#262626").place(x=255, y=0)

# ---------------------------------------------------------------------------------------------------------------------

'''mass=tk.Label(window, text="STATUS", bg="#5cb85c", fg="black", width=20,height=11, activebackground="orange",font=('Arial',15,'bold'))
mass.place(x=57,y=490)'''
# ---------------------------------------------SCROLLABLE FRAME FOR STATUS-------------------------------------------
main_frame = tk.LabelFrame(window)
main_frame.place(height=220, width=706, x=120, y=540)

wrapper = LabelFrame(main_frame)
mycanvas = Canvas(wrapper)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0, 0), wind=myframe, anchor="nw")
wrapper.pack(fill="both", expand="yes")

# -------------------------------------STATUS MESSAGE-----------------------------------------------

message = Label(myframe,
                text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
                fg="black", width=64, activebackground="orange", font=('calibri', 15))
message.config(anchor=CENTER)
message.pack()
# m=Label(myframe,text="hello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nhello my name is nikhil\nvvhello my name is nikhil\n",font=(30))
# m.pack()

message1 = Label(window, text="", width=50, fg="#ff4d4d", activebackground="orange", font=('calibri', 15))
message1.place(x=240, y=347)

message2 = Label(window, text="", fg="black", bg="white", width=70, activebackground="orange", font=('calibri', 15))
message2.place(x=120, y=448, height=34)


# -------------------------------SOME BUTTON FUNCTIONS--------------------------------------
def clear():
    txt.delete(0, 'end')
    res = ""
    message.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = ""
    message.configure(text=res)


def exitt():
    window.destroy()


def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(a)
        return True
    except(TypeError, ValueError):
        pass
    return False


# ----------------------------CHECk ALREADY REGISTERED DATA-------------------------
Branch = ['CS', 'ME', 'EE', 'BCA', 'MCA', 'ece', 'ECE', 'bba', 'PCM', 'pcm', 'cbz', 'CBZ', 'MBA', 'mba', 'Bcom', 'bca',
          'mca', 'cs', 'ee', 'me']


# ---------------------------------TAKING IMAGE----------------------------------
def TakeImages():
    Id = (txt.get())
    name = (txt2.get())
    br = 0
    if (name in Branch):
        br = 1

    # -----------------message erase-------------------------------
    message1.after(3000, lambda: message1.config(text=''))
    # ------------------------------------------------------

    wkbpath = "StudentDetails\\studentdetail.xlsx"
    wkb = openpyxl.load_workbook(wkbpath)

    sh = wkb['Sheet1']
    Columndata = []
    for c in sh.iter_cols(sh.min_column):
        for r in c:
            Columndata.append(r.value)
    ''''--------------------------STUDENT NAMES----------------------------------------------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
    '''student_records = {171022: "Nikhil Chaurasiya", 171038: "Shivam Gupta", 171001: "Abhishek Gupta",171049: "sudhanshu upadhyay",171044:"Shubham Gupta",171054:"yogita mishra",171034:"rishabh tiwari"}
    a = list(student_records.keys())
    -------------------------------------------------------------------------------------------------------------------------------------------'''

    if name == "cs" or name == "CS":
        stu_record_path = "students_added_records\\CS"
    elif name == "me" or name == "ME":
        stu_record_path = "students_added_records\\ME"
    elif name == "ee" or name == "EE":
        stu_record_path = "students_added_records\\EE"
    else:
        stu_record_path = "students_added_records"
    list_of_records = os.listdir(stu_record_path)

    # --------------------------------------------------------------------------------------
    if (is_number(Id) and br == 1 and int(Id) not in Columndata) and Id in list_of_records:

        file1 = open("students_added_records\\" + name.upper() + "\\" + Id, "r")
        verify = file1.read().splitlines()
        stu_name = verify[1]

        cam = cv2.VideoCapture(0)
        # harcascadePath="haarcascade_frontlface_default.xml"
        # detector=cv2.CascadeClassifier(harcascadePath)
        # detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        # face_cascade = cv2.CascadeClassifier('C:\\Python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # C:\Python\Lib\site-packages\cv2\data
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                cv2.imwrite("TrainingImages\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + h])
                cv2.imshow('Frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 20:
                break
        cam.release()
        cv2.destroyAllWindows()
        rollno = "0302" + str(name) + str(Id)
        Branch1 = name
        res = "Record saved for-   Rollno: " + rollno + "\tName: " + stu_name
        row = [Id, rollno, stu_name, Branch1]
        with open('StudentDetails\studentdetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message2.configure(text=res)
    else:
        if (str(name) not in Branch):
            res1 = "allowed only (cs,me,ee etc.)"
            message1.configure(text=res1)
        elif (is_number(Id)):
            res1 = "user already registered"
            message1.configure(text=res1)
        elif (name.isalpha()):
            res2 = "Id Must be Integer "
            message1.configure(text=res2)

        if (str(name) not in Branch):
            res1 = "allowed only (cs,me,ee etc.)"
            message1.configure(text=res1)
        elif str(Id) not in list_of_records:
            res1 = "invalid Id"
            message1.configure(text=res1)

        cot1 = 0
        if is_number(Id) in Columndata:
            cot1 = 1
        if (cot1 == 1):
            res3 = "(user already registered)"
            message1.configure(text=res3)


# ---------------------Progress Bar-------------------------------------------------------------------------------------
from tkinter.ttk import Progressbar

load = Progressbar(window, orient=HORIZONTAL, length=707, mode="determinate")


def wait():
    load['value'] = 20
    window.update_idletasks()
    time.sleep(0.1)

    load['value'] = 50
    window.update_idletasks()
    time.sleep(0.1)

    load['value'] = 70
    window.update_idletasks()
    time.sleep(0.1)

    load['value'] = 100
    window.update_idletasks()
    time.sleep(0.1)

    load['value'] = 150
    window.update_idletasks()
    time.sleep(0.1)


load.place(x=120, y=428)


# ---------------------TRAINING IMAGES------------------------------------------------
def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face, Id = getImagesAndLabels("TrainingImages")
    recognizer.train(face, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    wait()
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    message2.configure(text=res)


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNP = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNP)
        Ids.append((Id))
    return faces, Ids


# ---------- MATCH IMAGE FOR ATTENDANCE-----------------------------------------------------------

def TrackImage():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    # harcascadePath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    # faceCascade = cv2.CascadeClassifier(harcascadePath)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    df = pd.read_csv("StudentDetails\studentdetails.csv")
    cam = cv2.VideoCapture(0)
    cam.set(3, 1920)
    cam.set(4, 720)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Rollno', 'Name', 'Branch', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 60):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                Rno = df.loc[df['Id'] == Id]['Rollno'].values
                sbranch = df.loc[df['Id'] == Id]['Branch'].values
                sname = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "    " + Rno
                attendance.loc[len(attendance)] = [Id, Rno, sname, sbranch, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
                # if(conf > 50):
            #     noOfFile=len(os.listdir("ImagesUnknown"))+1
            #     cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Fetching Atendance', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance\Date_" + date + "_Time_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    message.configure(text=res)


# ---------- CSV TO XLSX -----------------------------------------------------------

df = pd.read_csv('StudentDetails\studentdetails.csv')
writer = pd.ExcelWriter('StudentDetails\studentdetail.xlsx')
df.to_excel(writer, index=False)
writer.save()

# ---------------------------------bUTTONS--------------------------------------
clrbtn = PhotoImage(file="iconImages\\clear.png")
btn_label = Label(image=clrbtn)
btn_label.pack()
# -----------------------------------------------------------------------------
clearButton = tk.Button(window, image=clrbtn, command=clear, borderwidth=0)
clearButton.place(x=785, y=253)

clearButton2 = tk.Button(window, image=clrbtn, command=clear2, borderwidth=0)
clearButton2.place(x=785, y=304)

takeImg = tk.Button(window, text=" TAKE IMAGE", command=TakeImages, fg="black", bg="orange", width=31,
                    activebackground="white", font=('arial', 15))
takeImg.place(x=120, y=378, height=50)

takeImg = tk.Button(window, text="TRAIN IMAGE", command=TrainImages, fg="black", bg="orange", width=31,
                    activebackground="white", font=('arial', 15))
takeImg.place(x=475, y=378, height=50)

takeImg = tk.Button(window, text="CLICK FOR ATTENDANCE", command=TrackImage, fg="white", bg="#5cb85c", width=58,
                    activebackground="white", font=('arial', 15, "bold"))
takeImg.place(x=120, y=490, height=50)

takeImg = tk.Button(window, text="Exit", command=exitt, fg="white", bg="#ff4d4d", width=41, height=2,
                    activebackground="white", font=('arial', 15))
takeImg.place(x=880, y=702)

# ***************************************************************************SIGN SIGNUP WHOLE FUNCTIONS******************************************************************************


'''-----------------------------------------ADD STUDENT ID & NAME--------------------------------------------------------------'''


def delete15():
    screen15.destroy()


def delete16():
    screen16.destroy()


def delete17():
    pin_update.destroy()

def delete18():
    pin_update_error.destroy()
def delete19():
    pass_update.destroy()
def delete20():
    pass_update_error.destroy()
def delete21():
    not_access.destroy()
def delete22():
    not_exist.destroy()
def delete23():
    alr_exist.destroy()
def delete24():
    acc_success.destroy()
def delete25():
    four_dig_error.destroy()
def stu_record_added_success():
    global screen16
    screen16 = Toplevel(screen3)
    screen16.overrideredirect(1)
    screen16.configure(background="#333333")
    screen16.geometry("350x200+950+190")
    Label(screen16, text="REGISTRATION SUCCESS", font=("calibri", 15), bg="#333333", fg="#33cc33").place(x=80, y=75)
    Button(screen16, text="OK", bg="#33cc33", font=("calibri", 15), fg="white", width=7, command=delete16).place(x=140,
                                                                                                                 y=120)


def add_student():
    stu_id_info = student_id.get()
    stu_name_info = student_name.get()
    stu_branch_info = student_branch.get()

    if stu_branch_info == "cs" or stu_branch_info == "CS":
        directory = os.listdir("students_added_records\\CS")
    elif stu_branch_info == "me" or stu_branch_info == "ME":
        directory = os.listdir("students_added_records\\ME")
    elif stu_branch_info == "ee" or stu_branch_info == "EE":
        directory = os.listdir("students_added_records\\ME")
    else:
        return None

    if (stu_id_info not in directory):

        file = open("students_added_records\\" + stu_branch_info.upper() + "\\" + stu_id_info, "w")
        file.write(stu_id_info + "\n")
        file.write(stu_name_info + "\n")
        file.write(stu_branch_info)
        file.close()

        student_id_entry.delete(0, END)
        student_name_entry.delete(0, END)
        student_branch_entry.delete(0, END)

        stu_record_added_success()
    else:
        global screen15
        screen15 = Toplevel(screen3)
        screen15.overrideredirect(1)
        screen15.configure(background="#333333")
        screen15.geometry("350x200+950+190")
        Label(screen15, text="ALREADY REGISTERED", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=90, y=75)
        Button(screen15, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete15).place(
            x=140, y=120)


# ------------------------------------------------------------------------------------------------------------------------------------

# ************************************************************************************************************************************************************************************
# add=Button(window, text="Add Student",width=45,bg="#5cb85c",fg="white",command=student,font=("arial",13,"bold"))
# add.place(x=1020,y=650,height=65)
def pin_successfully_updated():
    global pin_update
    pin_update = Toplevel(screen3)
    pin_update.overrideredirect(1)
    pin_update.configure(background="#333333")
    pin_update.geometry("350x200+945+245")
    Label(pin_update, text="PIN UPDATED SUCCESSFULLY", font=("calibri", 15), bg="#333333", fg="#33cc33").place(x=70,
                                                                                                               y=65)
    Button(pin_update, text="OK", bg="#33cc33", font=("calibri", 15), fg="white", width=7, command=delete17).place(
        x=140, y=110)

def access_denied_for_pin():
    global pin_update_error
    pin_update_error = Toplevel(screen3)
    pin_update_error.overrideredirect(1)
    pin_update_error.configure(background="#333333")
    pin_update_error.geometry("350x200+945+245")
    Label(pin_update_error, text="Access Denied", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=120,y=65)
    Button(pin_update_error, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete18).place(
        x=140, y=110)
def four_dig():
    global four_dig_error
    four_dig_error = Toplevel(screen3)
    four_dig_error.overrideredirect(1)
    four_dig_error.configure(background="#333333")
    four_dig_error.geometry("350x200+945+245")
    Label(four_dig_error, text="MUST BE 4 DIGIT", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=100, y=65)
    Button(four_dig_error, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7,
           command=delete25).place(
        x=140, y=110)
def pass_successfully_updated():
    global pass_update
    pass_update = Toplevel(screen3)
    pass_update.overrideredirect(1)
    pass_update.configure(background="#333333")
    pass_update.geometry("350x200+950+450")
    Label(pass_update, text="PASSWORD UPDATED SUCCESSFULLY", font=("calibri", 15), bg="#333333", fg="#33cc33").place(x=50,
                                                                                                               y=65)
    Button(pass_update, text="OK", bg="#33cc33", font=("calibri", 15), fg="white", width=7, command=delete19).place(
        x=140, y=110)
def pass_updated_error():
    global pass_update_error
    pass_update_error = Toplevel(screen3)
    pass_update_error.overrideredirect(1)
    pass_update_error.configure(background="#333333")
    pass_update_error.geometry("350x200+950+450")
    Label(pass_update_error, text="CURRENT PASSWORD INVALID", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=60,
                                                                                                               y=65)
    Button(pass_update_error, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete20).place(
        x=140, y=110)

def not_valid_user_for_access():
    global not_access
    not_access = Toplevel(screen3)
    not_access.overrideredirect(1)
    not_access.configure(background="#333333")
    not_access.geometry("350x180+945+507")
    Label(not_access, text="ACCESS DENIED", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=100,
                                                                                                               y=60)
    Button(not_access, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete21).place(
        x=140, y=105)
def user_not_exist():
    global not_exist
    not_exist = Toplevel(screen3)
    not_exist.overrideredirect(1)
    not_exist.configure(background="#333333")
    not_exist.geometry("350x180+945+507")
    Label(not_exist, text="USER NOT EXIST", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=70,
                                                                                                    y=60)
    Button(not_exist, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete22).place(
        x=140, y=105)
def already_access():
    global alr_exist
    alr_exist = Toplevel(screen3)
    alr_exist.overrideredirect(1)
    alr_exist.configure(background="#333333")
    alr_exist.geometry("350x180+945+507")
    Label(alr_exist, text="ACCESS ALREADY GIVEN", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=60,y=60)
    Button(alr_exist, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete23).place(
        x=140, y=105)
def access_successfully():
    global acc_success
    acc_success = Toplevel(screen3)
    acc_success.overrideredirect(1)
    acc_success.configure(background="#333333")
    acc_success.geometry("350x180+945+507")
    Label(acc_success, text="PERMITTED SUCCESSFULLY", font=("calibri", 15), bg="#333333", fg="#33cc33").place(x=60,
                                                                                                               y=60)
    Button(acc_success, text="OK", bg="#33cc33", font=("calibri", 15), fg="white", width=7, command=delete24).place(
        x=140, y=105)
def update_pin():
    security_email = os.listdir('login_details//head')
    email_file = open("login_details\\" + username1, "r")
    sec_verify = email_file.read().split()
    security_password=sec_verify[1]
    if username1 in security_email and password1==security_password:
        current_pin_info = current_pin.get()
        new_pin_info = new_pin.get()

        file1 = open("security_pin\\" + "pin", "r")
        verify = file1.read().splitlines()
        old_pin = verify[0]

        if current_pin_info == old_pin and len(current_pin_info) == 4 and len(new_pin_info) == 4:
            file1 = open("security_pin\\" + "pin", "w")
            file1.write(str(new_pin_info))

            current_pin_entry.delete(0, END)
            new_pin_entry.delete(0, END)
            pin_successfully_updated()
        else:
            four_dig()
    else:
        access_denied_for_pin()
def update_password():
    current_pass_info = current_pass.get()
    new_pass_info = new_pass.get()

    filepass = open("login_details\\" + username1, "r")
    verify = filepass.read().splitlines()
    old_pass = verify[1]

    if current_pass_info == old_pass:
        file1 = open("login_details\\" + username1, "w")
        file1.write(str(username1) + "\n")
        file1.write((str(new_pass_info)))

        current_pass_entry.delete(0, END)
        new_pass_entry.delete(0, END)
        pass_successfully_updated()
    else:
        pass_updated_error()

def give_access():
    access_email_info=access_email.get()
    mail_list=os.listdir('login_details//head')
    chk_AR_mail_list = os.listdir('login_details')
    if username1 in mail_list:
        if access_email_info in chk_AR_mail_list:
            if access_email_info not in mail_list:
                file_acc = open("login_details\\" +"head\\"+ access_email_info, "w")
                file_acc.write(str(access_email_info))

                access_email_entry.delete(0, END)
                access_successfully()
            else:
                already_access()
        else:
            user_not_exist()
    else:
        not_valid_user_for_access()

# --------------------DESTROYING SCREEN AFTER PRESSING OK AT THE TIME OF LOGIN----------------
def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def delete8():
    screen8.destroy()


def delete9():
    screen9.destroy()


def delete10():
    screen1.destroy()


def after_success():
    login()


# --------------------------MESSAGE AFTER LOGIN-----------------------------------------------
def login_success():
    global screen3
    global label_file
    global tv1
    screen3 = Toplevel(screen2)
    screen3.title("Manage Attendance")
    screen3.attributes('-fullscreen', True)
    screen3.geometry("1366x768+0+0")
    # ************************************************************VIEW ATTENDANCE***************************************************************************************************
    logo = tk.PhotoImage(
        file="iconImages\\glow-white-gradient-hexagon-black-1920x1080-c4-ffffff-ffffff-fffff0-000000-l2-1-27-a-10-f-6.png")
    BGlabel = tk.Label(screen3, image=logo)
    BGlabel.image = logo
    BGlabel.place(x=0, y=0, width=1600, height=900)

    Label(screen3, text="MANAGE STUDENTS RECORD AND ATTENDANCE", fg='white', bg="#202020", width="300", height="2",
          font=("arial", 20, "bold")).pack()

    def time2():
        string = strftime('%B %d ,%Y | %H :%M :%S %p')
        lbl5.config(text=string)
        lbl5.after(1000, time2)

    lbl5 = Label(screen3, font=('calibri', 18), background='#202020', foreground='white', height=1, width=128)
    lbl5.config(anchor=CENTER)
    lbl5.pack()
    time2()

    add_student_frame = LabelFrame(screen3, text="", borderwidth=4, bg="white")
    add_student_frame.place(x=940, y=150, height=250, width=377)

    pin_frame = LabelFrame(screen3, text="", borderwidth=4, bg="white")
    pin_frame.place(x=940, y=405, height=250, width=377)

    file_frame = tk.LabelFrame(screen3, bg="white")
    file_frame.place(height=170, width=870, x=60, y=150)

    frame3 = tk.LabelFrame(screen3, font=('arial', 15))
    frame3.place(height=450, width=870, x=60, y=260)
    # ------------------------------------Time-------------------------------------------------------------------------------

    # ------------------------------------------STUDENT DETAILS--------------------------------------------------------------
    global student_id
    global student_name
    global student_branch
    global student_id_entry
    global student_name_entry
    global student_branch_entry

    student_id = StringVar()
    student_name = StringVar()
    student_branch = StringVar()

    global new_pin
    global current_pin
    global new_pin_entry
    global current_pin_entry

    global new_pass
    global current_pass
    global new_pass_entry
    global current_pass_entry

    global access_email
    global access_email_entry
    access_email=StringVar()

    current_pass = StringVar()
    new_pass = StringVar()

    current_pin = StringVar()
    new_pin = StringVar()

    Label(file_frame, text="BROWSE ATTENDANCE FOR VIEW", fg='white', bg="#383838", width="870", height="1",
          font=("calibri", 18)).pack()
    # --------------------------------------------------ADD STUDENT----------------------------------------------------------------------
    Label(add_student_frame, text="ADD STUDENT DETAIL", fg='white', bg="#383838", width="30",
          font=("calibri", 18)).pack()

    Label(add_student_frame, text="ID:", bg="grey", fg="white", font=("Arial", 15)).place(x=20, y=55, width=100,
                                                                                          height=35)
    student_id_entry = Entry(add_student_frame, textvariable=student_id, width=25, font=("arial", 18), borderwidth="3")
    student_id_entry.place(x=110, y=55, width=240)

    Label(add_student_frame, text="NAME:", fg="white", bg="grey", font=("Arial", 15)).place(x=20, y=100, width=100,
                                                                                            height=35)
    student_name_entry = Entry(add_student_frame, textvariable=student_name, borderwidth="3", font=("arial", 18),
                               width=25)
    student_name_entry.place(x=110, y=100, width=240)

    Label(add_student_frame, text="Branch:", bg="grey", fg="white", font=("Arial", 15)).place(x=20, y=150, width=100,
                                                                                              height=35)
    student_branch_entry = Entry(add_student_frame, textvariable=student_branch, width=25, font=("arial", 18),
                                 borderwidth="3")
    student_branch_entry.place(x=110, y=150, width=240)

    Button(add_student_frame, text="ADD", width=15, bg="orange", font=("calibri", 16), command=add_student).place(x=100,y=190)

    def destroy_additional():
        Additional_options.destroy()
    # --------------------------------------------UPDATE PIN----------------------------------------------------------------------------
    def additional():
        global Additional_options
        global new_pin_entry
        global current_pin_entry

        global access_email_entry

        Additional_options = Toplevel(screen2)
        Additional_options.title("Manage Attendance")
        Additional_options.geometry("385x560+932+149")
        Additional_options.overrideredirect(1)
        Additional_options.configure(background="#ebfaeb")
        Label(Additional_options, text="FOR HOD AND PERMITTED USER", fg='white', bg="#383838", width="35", font=("calibri", 17)).pack()
        Button(Additional_options, text="X", height="1", fg='white', command=destroy_additional, bg='red', font=("calibri", 11), width=3).place(x=350, y=0)
#--------------------------------------------------------UPDATE PIN-------------------------------------------------
        update_pin_frame = LabelFrame(Additional_options, text="", borderwidth=4, bg="white")
        update_pin_frame.place(x=5, y=60, height=250, width=370)

        Label(Additional_options, text="UPDATE PIN", fg='white', bg="#5cb85c", width="30", font=("calibri", 15)).place(x=5,y=60,height=30,width=367)

        Label(Additional_options, text="CURRENT\nPIN", bg="#808080", fg="white", font=("Arial", 12)).place(x=20, y=125, width=100,height=40)
        current_pin_entry = Entry(Additional_options, textvariable=current_pin, width=25, font=("arial", 18), borderwidth="3")
        current_pin_entry.place(x=120, y=125, width=225, height=40)

        Label(Additional_options, text="NEW\nPIN", bg="#808080", fg="white", font=("Arial", 12)).place(x=20, y=180, width=100,height=40)
        new_pin_entry = Entry(Additional_options, textvariable=new_pin, width=25, font=("arial", 18), borderwidth="3")
        new_pin_entry.place(x=120, y=180, width=225, height=40)

        Button(Additional_options, text="UPDATE", width=15, bg="orange", font=("calibri", 16), command=update_pin).place(x=100,y=240)
#-------------------------------------GIVE ACCESS TO OTHER USER FOR PIN UPDATION----------------------------------------------
        G_access = LabelFrame(Additional_options, text="", borderwidth=4, bg="white")
        G_access.place(x=5, y=320, height=230, width=370)

        Label(Additional_options, text="ADD USER TO GIVE ACCESS", fg='white', bg="#5cb85c", width="30", font=("calibri", 15)).place(x=5, y=320, height=30, width=367)

        Label(Additional_options, text="EMAIL", bg="#808080", fg="white", font=("Arial", 12)).place(x=20, y=390, width=100,height=35)

        access_email_entry = Entry(Additional_options, textvariable=access_email, width=25, font=("arial", 18), borderwidth="3")
        access_email_entry.place(x=120, y=390, width=225, height=36)

        Button(Additional_options, text="ADD", width=15, bg="orange", font=("calibri", 16), command=give_access).place(x=100, y=470)


    #------------------------------------------UPDATE PASSWORD------------------------------------------------------------------
    Label(pin_frame, text="UPDATE YOUR PASSWORD", fg='white', bg="#383838", width="30", font=("calibri", 18)).pack()

    Label(pin_frame, text="CURRENT\nPASSWORD", bg="#808080", fg="white", font=("Arial", 12)).place(x=20, y=65, width=100,
                                                                                              height=40)
    current_pass_entry = Entry(pin_frame, textvariable=current_pass, width=25, font=("arial", 18), borderwidth="3")
    current_pass_entry.place(x=120, y=65, width=225, height=40)

    Label(pin_frame, text="NEW\nPASSWORD", bg="#808080", fg="white", font=("Arial", 12)).place(x=20, y=130, width=100,
                                                                                          height=40)
    new_pass_entry = Entry(pin_frame, textvariable=new_pass, width=25, font=("arial", 18), borderwidth="3")
    new_pass_entry.place(x=120, y=130, width=225, height=40)

    #Button(pin_frame, text="UPDATE", width=15, bg="orange", font=("calibri", 16), command=update_pin).place(x=100,
    #                                                                                                       y=180)

    Button(pin_frame, text="UPDATE", width=15, bg="orange", font=("calibri", 16), command=update_password).place(x=100,
                                                                                                                y=180)

    # -------------button--------------------------------

    log = tk.Button(screen3, text="View More Options", command=additional, fg="white", bg="#5cb85c", width=30, height=1,activebackground="white", font=('arial', 16))
    log.place(x=941, y=665)

    button5 = tk.Button(file_frame, text="Open attendence Sheet", fg="white", bg="#5cb85c", width=36, height=1,activebackground="orange", font=('arial', 15), command=lambda: [File_dialog()])
    button5.place(rely=0.40, relx=0.01)

    button6 = tk.Button(file_frame, text="View Sheet", fg="white", bg="#5cb85c", width=36, height=1,activebackground="orange", font=('arial', 15), command=lambda: Load_excel_data())
    button6.place(rely=0.40, relx=0.52)

    # The file/file path text
    label_file = ttk.Label(file_frame, text="NO FILE SELECTED", foreground="#ff4d4d", background="white")
    label_file.place(rely=0.28, relx=0.01)

    ## Treeview Widget
    tv1 = ttk.Treeview(frame3)
    tv1.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame3, orient="vertical", command=tv1.yview)
    treescrollx = tk.Scrollbar(frame3, orient="horizontal", command=tv1.xview)
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")

    def File_dialog():
        filename = filedialog.askopenfilename(initialdir="Attendance",
                                              title="Select A File",
                                              filetype=(
                                              ("csv files", "*.csv"), ("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        label_file["text"] = filename

    def Load_excel_data():
        file_path = label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)  # let the column heading = column name

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end",
                       values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

    '''log = tk.Button(screen3, text="LOGOUT", command=logout, fg="white", bg="#ff4d4d", width=30, height=1,activebackground="white", font=('arial', 16))
    log.place(x=941, y=665)'''
    log = tk.PhotoImage(
        file="iconImages\\inside-logout-icon.png")
    loglabel = tk.Label(screen3, image=log)
    loglabel.image = log
    BGlabel.pack()

    clearButton = tk.Button(screen3, image=log, command=logout,bg="#202020", borderwidth=0)
    clearButton.place(x=1240, y=20)
def logout():
    screen2.destroy()


def invalmail():
    invalidemail.destroy()


'''--------------------------------------------------------------------------------------------------------------------------------------------------------'''


def registration_success():
    global screen9
    screen9 = Toplevel(screen1)
    screen9.overrideredirect(1)
    screen9.configure(background="#333333")
    screen9.geometry("360x268+930+350")
    Label(screen9, text="REGISTRATION SUCCESS", font=("calibri", 15), bg="#333333", fg="#33cc33").place(x=80, y=75)
    Button(screen9, text="OK", bg="#33cc33", font=("calibri", 15), fg="white", width=7,
           command=lambda: [delete9(), delete10(), after_success()]).place(x=140, y=120)


def password_not_recognised():
    global screen4
    screen4 = Toplevel(window)
    screen4.overrideredirect(1)
    screen4.configure(background="#333333")
    screen4.geometry("360x268+930+350")
    Label(screen4, text="PASSWORD INCORRECT", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=80, y=75)
    Button(screen4, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete3).place(x=140,y=120)


def user_not_found():
    global screen5
    screen5 = Toplevel(window)
    screen5.overrideredirect(1)
    screen5.configure(background="#333333")
    screen5.geometry("360x268+930+350")
    Label(screen5, text="USER NOT FOUND", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=90, y=75)
    Button(screen5, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete4).place(x=140,y=120)


# ----------------------------SAVING A FILE OF USER REGISTRATION------------------------------------
def register_user():
    username_info = username.get()
    password_info = password.get()
    pin_info = pin.get()

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    chk = 0
    if (re.search(regex, username_info)):
        chk = 1
    else:
        chk = 0
    if (chk == 1):
        pin_folder_name = "pin"
        Pinfile = open("security_pin\\" + pin_folder_name, "r")
        verify_pin = Pinfile.read()

        if (pin_info == str(verify_pin)):
            directory = os.listdir("login_details")
            if (username_info not in directory):
                file = open("login_details\\" + username_info, "w")
                file.write(username_info + "\n")
                file.write(password_info)
                file.close()

                username_entry.delete(0, END)
                password_entry.delete(0, END)
                pin_entry.delete(0, END)

                registration_success()
            else:
                global screen8
                screen8 = Toplevel(window)
                screen8.overrideredirect(1)
                screen8.configure(background="#333333")
                screen8.geometry("360x268+930+350")
                Label(screen8, text="ALREADY REGISTERED", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=90,
                                                                                                                  y=75)
                Button(screen8, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7,
                       command=delete8).place(x=140, y=120)

        else:
            global screen6
            screen6 = Toplevel(window)
            screen6.overrideredirect(1)
            screen6.configure(background="#333333")
            screen6.geometry("360x268+930+350")
            Label(screen6, text="INCORRECT PIN", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=110, y=75)
            Button(screen6, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7, command=delete5).place(
                x=140, y=120)
    else:
        global invalidemail
        invalidemail = Toplevel(window)
        invalidemail.overrideredirect(1)
        invalidemail.configure(background="#333333")
        invalidemail.geometry("360x268+930+350")
        Label(invalidemail, text="INVALID EMAIL", font=("calibri", 15), bg="#333333", fg="#ff4d4d").place(x=110, y=75)
        Button(invalidemail, text="OK", bg="#ff4d4d", font=("calibri", 15), fg="white", width=7,
               command=invalmail).place(x=140, y=120)


# -----------------DESTROY REGISTRATION FAILED SCREEN-------------------------
def delete5():
    screen6.destroy()


# ------------------------------------------
# ---------------------------VERIFYING DETAILS AT THE TIME OF LOGIN-----------------------------------------
def login_verify():
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    pth = "login_details"
    list_of_files = os.listdir(pth)
    if username1 in list_of_files:
        file1 = open("login_details\\" + username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


# ---------------------------------DESTROY FOR LOGIN/LOGOUT--------------------------------------------------------------------
def des():
    screen.destroy()


def des1():
    screen2.destroy()


def des2():
    screen1.destroy()


# ------------------------------FOR REGISTRATION--------------------------------------
def register():
    global screen1
    screen1 = Toplevel(window)
    screen1.title("Register")
    screen1.geometry("468x482+875+180")
    screen1.configure(background="white")
    screen1.overrideredirect(1)

    global username
    global password
    global pin
    global username_entry
    global password_entry
    global pin_entry

    username = StringVar()
    password = StringVar()
    pin = StringVar()

    Label(screen1, text="REGISTRATION", fg='white', bg="#383838", width="300", height="1", font=("calibri", 16)).pack()
    Button(screen1, text="X", height="1", fg='white', command=des2, bg='red', font=("calibri", 11), width=4).place(x=425, y=0)

    div1 = LabelFrame(screen1, bg="white", borderwidth=3)
    div1.place(x=50, y=100, width=370, height=340)

    pathtophoto1 = Image.open("iconImages/registration1.png")
    image1 = ImageTk.PhotoImage(pathtophoto1)
    panel2 = Label(screen1, image=image1, bg="white")
    panel2.image = image1  # keep a reference
    panel2.pack(pady=10)

    pathtophoto2 = Image.open("iconImages/email.png")
    image2 = ImageTk.PhotoImage(pathtophoto2)
    panel3 = Label(screen1, image=image2, bg="white")
    panel3.image = image2  # keep a reference
    panel3.place(x=85, y=190)

    pathtophoto3 = Image.open("iconImages/password.png")
    image3 = ImageTk.PhotoImage(pathtophoto3)
    panel4 = Label(screen1, image=image3, bg="white")
    panel4.image = image3  # keep a reference
    panel4.place(x=85, y=260)

    username_entry = Entry(screen1, textvariable=username, width=25, font=("arial", 18), borderwidth="3")
    username_entry.place(x=130, y=190, width=240)

    password_entry = Entry(screen1, textvariable=password, show="*", borderwidth="3", font=("arial", 18), width=25)
    password_entry.place(x=130, y=263, width=240)

    lbl4 = tk.Label(screen1, text="****", height=1, bg="white", font=('calibri', 18))
    lbl4.place(x=220, y=300)

    pin_entry = Entry(screen1, textvariable=pin, show="*", borderwidth="3", font=("arial", 18))
    pin_entry.place(x=200, y=320, width=95)
    Button(screen1, text="REGISTER", width=15, bg="orange", height=1, font=("calibri", 16),command=register_user).place(x=160, y=365)


# ----------------------------FOR LOGIN-------------------------------------------------------------------------------
def login():
    global screen2
    screen2 = Toplevel(window)
    screen2.geometry("468x482+875+180")
    screen2.overrideredirect(1)
    screen2.configure(background="white")

    Label(screen2, text="LOGIN", fg='white', bg="#383838", width="300", height="1", font=("calibri", 16)).pack()
    Button(screen2, text="X", height="1", fg='white', command=des1, bg='red', font=("calibri", 11), width=4).place(x=425, y=0)

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    div = LabelFrame(screen2, bg="white", borderwidth=3)
    div.place(x=50, y=100, width=370, height=340)

    pathtophoto1 = Image.open("iconImages/login.png")
    image1 = ImageTk.PhotoImage(pathtophoto1)
    panel2 = Label(screen2, image=image1, bg="white")
    panel2.image = image1  # keep a reference
    panel2.pack(pady=10)

    pathtophoto2 = Image.open("iconImages/email.png")
    image2 = ImageTk.PhotoImage(pathtophoto2)
    panel3 = Label(screen2, image=image2, bg="white")
    panel3.image = image2  # keep a reference
    panel3.place(x=85, y=190)

    pathtophoto3 = Image.open("iconImages/password.png")
    image3 = ImageTk.PhotoImage(pathtophoto3)
    panel4 = Label(screen2, image=image3, bg="white")
    panel4.image = image3  # keep a reference
    panel4.place(x=85, y=260)

    username_entry1 = Entry(screen2, textvariable=username_verify, width=25, font=("arial", 18), borderwidth="3")
    username_entry1.place(x=130, y=190, width=240)

    password_entry1 = Entry(screen2, textvariable=password_verify, show="*", borderwidth="3", font=("arial", 18),width=25)
    password_entry1.place(x=130, y=263, width=240)
    Button(screen2, text="LOGIN", width=15, bg="orange", height=1, font=("calibri", 16), command=login_verify).place(x=157, y=330)


# --------------------------------FOR LOGIN/SIGNUP MAIN SCREEN------------------------------------------------------------------
def main_screen():
    global screen
    screen = Toplevel(window)
    screen.geometry("468x482+875+180")
    screen.overrideredirect(1)
    screen.configure(background='white')

    frame_login = Frame(screen, background='white')
    frame_login.place(x=0, y=30, width=470, height=440)

    login_sqr=LabelFrame(frame_login,borderwidth=5,bg="white")
    login_sqr.place(x=100,y=40,width=440,height=380)

    pathtophoto = Image.open("iconImages/user2.png")
    image1 = ImageTk.PhotoImage(pathtophoto)
    panel1 = Label(frame_login, image=image1, bg="white")
    panel1.image = image1  # keep a reference
    panel1.place(x=10,y=140)
    # img1 = ImageTk.PhotoImage(file="iconimages/user.png")
    # imgl2 = Label(screen2, image=img1).pack()

    Label(screen, text="FOR MANAGE ATTENDANCE & RECORD", fg='white', bg="#383838", width="300", height="1",font=("calibri", 16)).pack()
    Button(screen, text="X", height="1", fg='white', command=des, bg='red', font=("calibri", 11), width=4).place(x=425,y=0)

    Button(screen, text="LOGIN", height="2", fg='white', bg='orange', width="15", command=login,
           font=("arial", 13)).place(x=300, y=165)
    Button(screen, text="REGISTER", height="2", fg='white', bg='orange', width="15", command=register,
           font=("arial", 13)).place(x=300, y=295)


# --------------------------VIEW ATTENDANCE FRAME----------------------------------------------------------------------------------------------------------------

imge = ImageTk.PhotoImage(file="iconimages/grp.jpg")
imgl = Label(window, image=imge, bg="white").place(x=880, y=348, width=455, height=250)

b = Button(window, text="MANAGE ATTENDANCE & \n RECORDS", width=45, bg="#5cb85c", fg="white", command=main_screen,font=("arial", 13, "bold"))
b.place(x=880, y=596, height=65)

'''------------------------------NOTE-------------------------------------------------------------'''
fram = LabelFrame(window, text="", bg="#ffffff", borderwidth=3, relief='groove')
fram.place(x=880, y=180, height=140, width=455)

mess = Label(fram, text="NOTE", font=("calibri", 21), bg="#ff4d4d", fg="white", width=32, relief=RAISED)
mess.config()
mess.pack()
mess = Label(fram, text="1. Press 'Q' to quit the camera after giving attendance.", font=("calibri", 13), bg="#ffffff",fg="red")
mess.config()
mess.pack()
mess = Label(fram,text="2. Press 'Alt+tab' once while open attendance sheet     \nfor return to the manage page.",font=("calibri", 13), bg="#ffffff", fg="red")
mess.config()
mess.pack()

# -------------------------------FOOTER--------------------------------------------------------------
'''
footer = Label(window,text="Developed By Nikhil & Shivam", font=('calibri', 12),background='orange',foreground='white',height=1,width=200)
footer.config(anchor=CENTER)
footer.place(y=773)
'''
window.mainloop()