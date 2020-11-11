from tkinter import *
from tkinter  import messagebox
from tkinter.filedialog import askopenfile
import smtplib, time, os
root = Tk()
server = StringVar()
port = [587, 465]
smtpObj = ""
server_frame = Frame(borderwidth= 5)
login_frame = Frame(padx = 5, bg = "grey")
file_frame = Frame()
filenamepath ="None Selected......"

Gmail = Radiobutton(server_frame, text="Gmail", variable = server, value="smtp.gmail.com", tristatevalue = "x", borderwidth = 2, relief = "groove" )
Yahoo = Radiobutton(server_frame, text="Yahoo", variable = server, value="smtp.mail.yahoo.com", tristatevalue = "x", borderwidth = 2, relief = "groove" )
Outlook = Radiobutton(server_frame, text="Outlook", variable = server, value="smtp-mail.outlook.com", tristatevalue = "x", borderwidth = 2, relief = "groove" )
ATaT = Radiobutton(server_frame, text="AT&T", variable = server, value="smtp.mail.att.net", tristatevalue = "x", borderwidth = 2, relief = "groove" )
Comcast = Radiobutton(server_frame, text="Comcast", variable = server, value="smtp.comcast.net", tristatevalue = "x", borderwidth = 2, relief = "groove" )
Verizon = Radiobutton(server_frame, text="Verizon", variable = server, value="smtp.verizon.net", tristatevalue = "x", borderwidth = 2, relief = "groove" )
def account():
    if len(email_box.get()) >= 7 and len(password_box.get()) >= 8:
        emailadd = email_box.get()
        passcode = password_box.get()
        smtpObj.login(emailadd, passcode)

def openfile():
    file = askopenfile(mode = "r", filetypes = [("Veritext file", "*.vtx")])

    if file  is not None:
        content = file.read()
        filenamepath = file.name
        file_label.configure(text= filenamepath)

def login():
    try:
        if len(server.get()) > 0:
            global smtpObj
            for i in range(2):
                smtpObj = smtplib.SMTP(server.get(), port[i])
                if type(smtpObj) == smtplib.SMTP:
                    smtpObj.ehlo()
                    break
                    if i == 0:
                        starttls()
                    else:
                        continue
                    account()
        else:
            messagebox.showerror("Error", "Please select a server")

    except:
        messagebox.showerror("Error", 'Check your internet connection \n If Problem persists, refer to the administrator')


#Define File button and labels
fileopen = Button(file_frame, text="Load file", font=("Calibri", 12), command= openfile)
file_label = Label(file_frame,text=filenamepath, font=("Calibri", 12),  relief="flat", highlightcolor = "black", highlightthickness = 1, padx= 20, highlightbackground ="red")


#Defining Entry Labels
password_box = Entry(login_frame, font=("Calibri", 10), width=15, show="*", highlightcolor = "black", highlightthickness = 2, borderwidth = 3)
email_box = Entry(login_frame, font=("Calibri", 8), width=40, borderwidth = 3, highlightcolor = "black", highlightthickness = 2)
mail_box = Text(font=("Calibri", 10), width=90, height=20, highlightcolor = "black", highlightthickness = 2, borderwidth = 3)

#Defining Labels
password_label= Label(login_frame, text="Enter Your Password: ", font=("Calibri", 12),  relief="flat", highlightcolor = "black", highlightthickness = 1, highlightbackground ="red")
email_label= Label(login_frame, text="Enter Your Email: ", font=("Calibri", 12))

#Defining login button
login_but = Button(login_frame, text="Log In", font=("Calibri", 12), command= login)

#Grid Server name in Frame
Gmail.grid(row= 0, column= 0, padx = 20)
Yahoo.grid(row = 0, column=1, padx = 20)
Outlook.grid(row = 0, column=2, padx = 20)
ATaT.grid(row = 0, column=3, padx = 20)
Comcast.grid(row = 0, column=4, padx = 20)
Verizon.grid(row = 0, column=5, padx = 20)

#Grid server_frame in window
server_frame.grid(row=0, column= 0)

#Grid login_labels and login_entries in login_frame
email_label.grid(row= 0, column= 0)
email_box.grid(row=0, column=1)
password_label.grid(row= 0, column= 2)
password_box.grid(row= 0, column= 3)
login_but.grid(row=0, column = 4)

#Grid login_frame
login_frame.grid(row=1, column= 0)

#Grid file frame 
file_frame.grid(row=2, column = 0)

#Grid file buttons and labels
fileopen.grid(row=0, column = 0)
file_label.grid(row=0, column= 1)

#Grid email buttons
mail_box.grid(row=3, column = 0)

root.title("Batch-mail")
root.geometry("700x600")
mainloop()
            


    


