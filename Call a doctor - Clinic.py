import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox, simpledialog,  Button
from PIL import ImageTk, Image

LARGEFONT = ("Verdana", 35)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.clinic_id = None

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginClinic, RegisterClinic, RegisterFounder, ClinicAccount, ClinicPending, ClinicHomepage, UploadDoctor
                  , ManageDoctor, DoctorList, ClinicDecline, ClinicInfo,DoctorMainpage,PrescriptionPage,ViewPrescriptionsPage,ManagePrescriptionsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginClinic)

    def show_frame(self, frame_class):
        print(self.clinic_id)
        frame = self.frames[frame_class]
        frame.clinic_id = self.clinic_id 
        frame.tkraise()
        if isinstance(frame, ClinicInfo):
            frame.showclinicdetails()
        if isinstance(frame, DoctorList):
            frame.showdoctordetails()
        if isinstance(frame, ManageDoctor):
            frame.showdoctordetails()
        if isinstance(frame, ClinicPending):
            frame.display_status()
        if isinstance(frame, ClinicDecline):
            frame.display_status()
        if isinstance(frame, ClinicHomepage):
            frame.showappointmentdetails()

class LoginClinic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        clinic_username = StringVar()

        self.login_clinic = tk.Frame(self, background="white")
        self.login_clinic.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = tk.Label(self.login_clinic, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = tk.Label(self.login_clinic, text="Clinic Login", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=416, y=160)

        self.clnloginusername_label = tk.Label(self.login_clinic, text="Username", font=(25), background="white")
        self.clnloginusername_label.place(x=330, y=250)
        self.clnloginusername_entry = tk.Entry(self.login_clinic, textvariable=clinic_username)
        self.clnloginusername_entry.place(height=30, width=350, x=330, y=275)

        self.clnloginpassword_label = tk.Label(self.login_clinic, text="Password", font=(25), background="white")
        self.clnloginpassword_label.place(x=330, y=350)
        self.clnloginpassword_entry = tk.Entry(self.login_clinic)
        self.clnloginpassword_entry.place(height=30, width=350, x=330, y=375)

        login_btn = tk.Button(self.login_clinic, text="Login", background="thistle", command=self.login)
        login_btn.place(height=30, width=100, x=447, y=470)

        goRegister_btn = tk.Button(self.login_clinic, text="Don't have an account ?", font=('Helvetica', 13), borderwidth=0, background="white", command=lambda: controller.show_frame(RegisterClinic))
        goRegister_btn.place(height=30, width=250, x=380, y=610)

    def login(self):
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if self.clnloginusername_entry.get() == "" or self.clnloginpassword_entry.get() == "":
            messagebox.showerror("Error", "Please fill in all the fields")
        else:
            cursor.execute("SELECT * FROM ClinicInformation WHERE clinic_username = ? AND clinic_password = ?", (self.clnloginusername_entry.get(), self.clnloginpassword_entry.get()))
            rows = cursor.fetchall()
            if rows:
                status = rows[0][13] 
                if status == 1:
                    self.controller.clinic_id = rows[0][0]
                    messagebox.showinfo("Success", "Login Successful")
                    self.controller.show_frame(ClinicHomepage)
                elif status == 2:
                    self.controller.clinic_id = rows[0][0]
                    messagebox.showerror("Info", "Login Declined")
                    self.controller.show_frame(ClinicDecline)
                elif status == 0:
                    self.controller.clinic_id = rows[0][0]
                    messagebox.showinfo("Info", "Login Pending")
                    self.controller.show_frame(ClinicPending)
                else:
                    messagebox.showerror("Error", "Invalid Username or Password")
                    return
                self.clnloginusername_entry.delete(0, 'end')
                self.clnloginpassword_entry.delete(0, 'end')
            else:
                messagebox.showerror("Error", "Invalid Username or Password")

        conn.commit()
        conn.close()

class RegisterClinic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.register_clinic = Frame(self, background="white")
        self.register_clinic.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.register_clinic, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = Label(self.register_clinic, text="Clinic Information", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=374, y=160)

        self.clinicname_label = Label(self.register_clinic, text="Clinic name", font=(25), background="white")
        self.clinicname_label.place(x=100, y=230)
        self.clinicname_label_entry = Entry(self.register_clinic)
        self.clinicname_label_entry.place(height=30, width=820, x=100, y=255)

        self.clinictime_label = Label(self.register_clinic, text="Clinic operation time", font=(25), background="white")
        self.clinictime_label.place(x=100, y=310)
        self.clinictime_label_entry = Entry(self.register_clinic)
        self.clinictime_label_entry.place(height=30, width=350, x=100, y=335)

        self.cliniccoordinates_label = Label(self.register_clinic, text="Clinic location coordinates", font=(25), background="white")
        self.cliniccoordinates_label.place(x=100, y=390)
        self.cliniccoordinates_label_entry = Entry(self.register_clinic)
        self.cliniccoordinates_label_entry.place(height=30, width=350, x=100, y=415)

        self.clinicaddress_label = Label(self.register_clinic, text="Clinic address", font=(25), background="white")
        self.clinicaddress_label.place(x=100, y=470)
        self.clinicaddress_label_entry = Entry(self.register_clinic)
        self.clinicaddress_label_entry.place(height=80, width=350, x=100, y=495)

        self.cliniccontact_label = Label(self.register_clinic, text="Clinic contact number", font=(25), background="white")
        self.cliniccontact_label.place(x=570, y=310)
        self.cliniccontact_label_entry = Entry(self.register_clinic)
        self.cliniccontact_label_entry.place(height=30, width=350, x=570, y=335)

        self.clinicregno_label = Label(self.register_clinic, text="Clinic registration nummber", font=(25), background="white")
        self.clinicregno_label.place(x=570, y=390)
        self.clinicregno_label_entry = Entry(self.register_clinic)
        self.clinicregno_label_entry.place(height=30, width=350, x=570, y=415)

        self.clinicdesc_label = Label(self.register_clinic, text="Clinic description", font=(25), background="white")
        self.clinicdesc_label.place(x=570, y=470)
        self.clinicdesc_label_entry = Entry(self.register_clinic)
        self.clinicdesc_label_entry.place(height=80, width=350, x=570, y=495)

        nxtTOfounder_btn = Button(self.register_clinic, text = "Next", background="thistle",command=self.go_to_next_page)
        nxtTOfounder_btn.place(height=30, width=100,x=450, y=590)

    def go_to_next_page(self):
        clinic_information = self.get_clinic_information()
        if clinic_information[0] == "" or clinic_information[1] == "" or clinic_information[2] == "" or clinic_information[3] == "" or clinic_information[4] == "" or clinic_information[5] == "" or clinic_information[6] == "":
            messagebox.showerror("Error", "Please fill in all the fields")
        else:
            self.controller.show_frame(RegisterFounder)

    def get_clinic_information(self):
        clinic_name = self.clinicname_label_entry.get()
        clinic_time = self.clinictime_label_entry.get()
        clinic_coordinates = self.cliniccoordinates_label_entry.get()
        clinic_address = self.clinicaddress_label_entry.get()
        clinic_contact= self.cliniccontact_label_entry.get()
        clinic_registration_no = self.clinicregno_label_entry.get()
        clinic_description = self.clinicdesc_label_entry.get()
        return clinic_name, clinic_time, clinic_coordinates, clinic_address, clinic_contact, clinic_registration_no, clinic_description

class RegisterFounder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.register_founder = Frame(self, background="white")
        self.register_founder.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.register_founder, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = Label(self.register_founder, text="Clinic's Founder Information", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=310, y=160)

        self.foundername_label = Label(self.register_founder, text="Founder full name", font=(25), background="white")
        self.foundername_label.place(x=330, y=250)
        self.foundername_label_entry = Entry(self.register_founder)
        self.foundername_label_entry.place(height=30, width=350, x=330, y=275)

        self.foundercontact_label = Label(self.register_founder, text="Founder contact", font=(25), background="white")
        self.foundercontact_label.place(x=330, y=350)
        self.foundercontact_label_entry = Entry(self.register_founder)
        self.foundercontact_label_entry.place(height=30, width=350, x=330, y=375)

        self.founderemail_label = Label(self.register_founder, text="Founder email address", font=(25), background="white")
        self.founderemail_label.place(x=330, y=450)
        self.founderemail_label_entry = Entry(self.register_founder)
        self.founderemail_label_entry.place(height=30, width=350, x=330, y=475)

        nxtTOsignup_btn = Button(self.register_founder, text = "Next",background="thistle",command=self.go_to_account_page)
        nxtTOsignup_btn.place(height=30, width=100,x=450, y=570)

    def go_to_account_page(self):
        founder_information = self.get_clinic_founder()
        if founder_information[0] == "" or founder_information[1] == "" or founder_information[2] == "":
            messagebox.showerror("Error", "Please fill in all the fields")
        else:
            self.controller.show_frame(ClinicAccount)

    def get_clinic_founder(self):
        founder_name = self.foundername_label_entry.get()
        founder_contact = self.foundercontact_label_entry.get()
        founder_email = self.founderemail_label_entry.get()
        return founder_name, founder_contact, founder_email

class ClinicAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.clinic_account = Frame(self, background="white")
        self.clinic_account.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.clinic_account, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = Label(self.clinic_account, text="Clinic Sign Up", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=416, y=145)

        self.clnregusername_label = Label(self.clinic_account, text="Username", font=(25), background="white")
        self.clnregusername_label.place(x=330, y=250)
        self.clnregusername_label_entry = Entry(self.clinic_account)
        self.clnregusername_label_entry.place(height=30, width=350, x=330, y=275)

        self.clnregpassword_label = Label(self.clinic_account, text="Password", font=(25), background="white")
        self.clnregpassword_label.place(x=330, y=350)
        self.clnloginpassword_label_entry = Entry(self.clinic_account)
        self.clnloginpassword_label_entry.place(height=30, width=350, x=330, y=375)

        clinicsignup_btn = Button(self.clinic_account, text="Send request to Call A Doctor", background="thistle",
                                  command=self.submit_clinic_registration)
        clinicsignup_btn.place(height=30, width=250, x=380, y=470)

    def submit_clinic_registration(self):
        clinic_username = self.clnregusername_label_entry.get()
        clinic_password = self.clnloginpassword_label_entry.get()
        if not clinic_username or not clinic_password:
            messagebox.showerror("Error", "Please fill in both the username and password fields")
            return
        clinic_information = self.controller.frames[RegisterClinic].get_clinic_information()
        clinic_founder = self.controller.frames[RegisterFounder].get_clinic_founder()
        clinic_username = self.clnregusername_label_entry.get()
        clinic_password = self.clnloginpassword_label_entry.get()

        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ClinicInformation (
                clinic_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                clinic_name TEXT NOT NULL,
                clinic_operation_time TEXT NOT NULL,
                clinic_coordinates TEXT NOT NULL,
                clinic_address TEXT NOT NULL,
                clinic_contact INT NOT NULL,
                clinic_registration_no INT NOT NULL,
                clinic_description TEXT NOT NULL,
                founder_name TEXT NOT NULL,
                founder_contact INT NOT NULL,
                founder_email TEXT NOT NULL,
                clinic_username TEXT NOT NULL,
                clinic_password TEXT NOT NULL,
                status INT NOT NULL          
            )
        ''')

        cursor.execute('''
            INSERT INTO ClinicInformation (clinic_name, clinic_operation_time, clinic_coordinates,
                                        clinic_address, clinic_contact, clinic_registration_no,
                                        clinic_description, founder_name, founder_contact,
                                        founder_email, clinic_username, clinic_password, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (clinic_information[0], clinic_information[1], clinic_information[2], clinic_information[3],
            clinic_information[4], clinic_information[5], clinic_information[6], clinic_founder[0],
            clinic_founder[1], clinic_founder[2], clinic_username, clinic_password, 0))
        
        self.controller.clinic_id = cursor.lastrowid
        messagebox.showinfo("Success", "Clinic registration successful")

        conn.commit()
        conn.close()

        self.controller.show_frame(ClinicPending)

class ClinicPending(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.clinic_pending = Frame(self, background="white")
        self.clinic_pending.place(height=700, width=1000, x=0, y=0)

        
        self.topframe = Frame(self.clinic_pending, background="cornsilk")
        self.topframe.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg")
        label_width, label_height = 50, 50
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS for resizing
        # Create a PhotoImage from the resized image
        image = ImageTk.PhotoImage(image)

        label = Label(self.topframe, image=image)
        label.image = image  # Keep a reference to the image to prevent garbage collection
        label.place(height=label_height, width=label_width, x=25, y=25)

        self.topframe_label = Label(self.topframe, text="Clinic Pending", font=("Helvetica", 25, "bold"), background="cornsilk")
        self.topframe_label.place(x=130, y=20)

        self.centerframe = Frame(self.clinic_pending, background="white", bd=12, relief=RIDGE)
        self.centerframe.place(height=610, width=1000, x=0, y=90)

        self.innercenterframe = Frame(self.centerframe, background="thistle")
        self.innercenterframe.place(height=540, width=930, x=30, y=30)

        self.clinicLogout_btn = Button(self.topframe, text="Logout", background="thistle", command=lambda: controller.show_frame(LoginClinic))
        self.clinicLogout_btn.place(height=30, width=60, x=910, y=25)

        self.pending_label = Label(self.innercenterframe, text="Please wait. Your account is being processed.", font=(15), background="cornsilk")
        self.pending_label.place(height=70,width=480, x=200, y=300) 

    def display_status(self):
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        clinic_id = self.clinic_id
        cursor.execute("SELECT status, clinic_name FROM ClinicInformation WHERE clinic_id = ?", (clinic_id,))
        rows = cursor.fetchall()

        status = rows[0][0]
        status = int(status)
        if status == 0:
            status = "Pending"
        clinic_name = rows[0][1]
        clinicname = tk.Label(self.innercenterframe, text="Dear " + str(clinic_name), font=(15), background="cornsilk")
        clinicname.place(height=70,width=480, x=200, y=100)
        
        status = tk.Label(self.innercenterframe, text="Account Status: " + str(status), font=(15), background="cornsilk")
        status.place(height=70,width=480, x=200, y=200)

        conn.commit()
        conn.close()

class ClinicDecline(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.clinic_decline = Frame(self, background="white")
        self.clinic_decline.place(height=700, width=1000, x=0, y=0)

        self.topframe = Frame(self.clinic_decline, background="cornsilk")
        self.topframe.place(height=90, width=1000, x=0, y=0)

        self.topframe_label = Label(self.topframe, text="Clinic Decline", font=("Helvetica", 25, "bold"), background="cornsilk")
        self.topframe_label.place(x=130, y=20)

        image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg")
        label_width, label_height = 50, 50
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS for resizing
        # Create a PhotoImage from the resized image
        image = ImageTk.PhotoImage(image)

        label = Label(self.topframe, image=image)
        label.image = image  # Keep a reference to the image to prevent garbage collection
        label.place(height=label_height, width=label_width, x=25, y=25)

        self.topframe_label = Label(self.topframe, text="Clinic Pending", font=("Helvetica", 25, "bold"), background="cornsilk")
        self.topframe_label.place(x=130, y=20)

        self.centerframe = Frame(self.clinic_decline, background="white", bd=12, relief=RIDGE)
        self.centerframe.place(height=610, width=1000, x=0, y=90)

        self.innercenterframe = Frame(self.centerframe, background="thistle")
        self.innercenterframe.place(height=540, width=930, x=30, y=30)

        self.clinicLogout_btn = Button(self.topframe, text="Logout", background="thistle", command=lambda: controller.show_frame(LoginClinic))
        self.clinicLogout_btn.place(height=30, width=60, x=910, y=25)

        self.decline_label = Label(self.innercenterframe, text="Sorry, Your request has been decline", font=(15), background="thistle")
        self.decline_label.place(height=70,width=480, x=200, y=280) 
    
    def display_status(self):
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        clinic_id = self.clinic_id
        cursor.execute("SELECT status, clinic_name, reason FROM ClinicInformation WHERE clinic_id = ?", (clinic_id,))
        rows = cursor.fetchall()

        status = rows[0][0]
        status = int(status)
        if status == 2:
            status = "Decline"
        clinic_name = rows[0][1]
        reason = rows[0][2]
        clinicname = tk.Label(self.innercenterframe, text="Dear " + str(clinic_name), font=(15), background="cornsilk")
        clinicname.place(height=70, width=480, x=200, y=50)
        
        status = tk.Label(self.innercenterframe, text=" Account Status: " + str(status), font=(15), background="cornsilk")
        status.place(height=70, width=480, x=200, y=120)

        self.decline_reason = Label(self.innercenterframe, text="Reason: " + str(reason), font=(15), background="cornsilk",anchor="center",wraplength=300)
        self.decline_reason.place(height=100, width=480, x=200, y=190)

        conn.commit()
        conn.close()

class ClinicHomepage(LoginClinic, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.clinic_id = None

        self.clinic_homepage = tk.Frame(self, background="white")
        self.clinic_homepage.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = tk.Frame(self.clinic_homepage, background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(self.clinic_homepage, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = tk.Label(self.clinic_homepage, text="Clinic Home", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicLogout_btn = tk.Button(self.clinic_homepage, text="Logout", background="thistle", command=lambda: controller.show_frame(LoginClinic))
        clinicLogout_btn.place(height=30, width=60, x=910, y=25)

        self.clinicleft_frame = tk.Frame(self.clinic_homepage, background="cornsilk")
        self.clinicleft_frame.place(height=530, width=320, x=40, y=130)

        uploadDoctor_btn = tk.Button(self.clinic_homepage, text=" Upload Doctor ", font=(20), background="white", command=lambda: controller.show_frame(UploadDoctor))
        uploadDoctor_btn.place(height=70, width=200, x=100, y=170)

        manageDoctor_btn = tk.Button(self.clinic_homepage, text=" Manage Doctor ", font=(20), background="white", command=lambda: controller.show_frame(ManageDoctor))
        manageDoctor_btn.place(height=70, width=200, x=100, y=290)

        viewDoctor_btn = tk.Button(self.clinic_homepage, text=" Doctor List ", font=(20), background="white", command=lambda: controller.show_frame(DoctorList))
        viewDoctor_btn.place(height=70, width=200, x=100, y=410)

        viewClinic_btn = tk.Button(self.clinic_homepage, text=" About Us ", font=(20), background="white", command=lambda: controller.show_frame(ClinicInfo))
        viewClinic_btn.place(height=70, width=200, x=100, y=530)

        self.clinicright_frame = tk.Frame(self.clinic_homepage, background="cornsilk")
        self.clinicright_frame.place(height=530, width=540, x=410, y=130)

        self.patient_label = tk.Label(self.clinic_homepage, text="Patient", font=(25), background="white")
        self.patient_label.place(height=70, width=480, x=440, y=160)

        self.refreshappointment_btn = tk.Button(self.clinic_homepage, text="Refresh", background="cornsilk", command=self.refreshappointment, borderwidth=0)
        self.refreshappointment_btn.place(height=20, width=60, x=850, y=240)

        self.appointmentlist_canvas = Canvas(self.clinic_homepage, background="white", bd=0, highlightthickness=0)
        self.appointmentlist_canvas.place(height=350, width=460, x=440, y=260)

        self.appointmentlist_scrollbar = Scrollbar(self.clinic_homepage, orient="vertical", command=self.appointmentlist_canvas.yview)
        self.appointmentlist_scrollbar.place(height=350, width=20, x=900, y=260)

        self.appointmentlist_canvas.configure(yscrollcommand=self.appointmentlist_scrollbar.set)

        self.appointmentframe_inner = Frame(self.appointmentlist_canvas, background="white")
        self.appointmentlist_canvas.create_window((0, 0), window=self.appointmentframe_inner, anchor="nw")

        self.appointmentframe_inner.bind('<Configure>', lambda e: self.appointmentlist_canvas.configure(scrollregion=self.appointmentlist_canvas.bbox("all")))

        self.showappointmentdetails()

    def refreshappointment(self):
        self.appointmentframe_inner.destroy()
        self.appointmentframe_inner = Frame(self.appointmentlist_canvas, background="white")
        self.appointmentlist_canvas.create_window((0, 0), window=self.appointmentframe_inner, anchor="nw")
        self.showappointmentdetails()

    def showappointmentdetails(self):
        clinic_id = self.clinic_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Appointment.symptoms, PatientInfo.PatientName, PatientInfo.patID, Appointment.appointment_id FROM Appointment 
            JOIN PatientInfo ON Appointment.patID = PatientInfo.patID 
            WHERE Appointment.clinic_id = ? AND appointment_status = 0""", (clinic_id,))
        display_appointment = cursor.fetchall()
        i=0
        for appointment in display_appointment:
            appointment_frame = Frame(self.appointmentframe_inner, background="white", highlightbackground="orange", highlightthickness=1, width=459, height=70)
            appointment_frame.grid(row=i, column=0, padx=1, pady=1)
            patient_name = Label(appointment_frame, text=appointment[1], font=(15), background="white")
            patient_name.place(x=10, y=5)
            symptoms = Label(appointment_frame, text="Symptoms: " + appointment[0], font=(15), background="white")
            symptoms.place(x=10, y=35)
            view_patient_button = Button(appointment_frame, text="View Patient", command=lambda appointment_id=appointment[3]: self.viewpatient(appointment_id), background="white", fg="blue", borderwidth=0)
            view_patient_button.place(height=20, width=70, x=380, y=25)
            i+=1
        conn.close()

    def viewpatient(self, appointment_id):
        clinic_id = self.clinic_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT patID FROM Appointment WHERE appointment_id = ?", (appointment_id,))
        fetch_result = cursor.fetchone()
        if fetch_result is not None:
            patID = fetch_result[0]
        else:
            patID = None
        cursor.execute("SELECT PatientName, ContactNumber FROM PatientInfo WHERE patID = ?", (patID,))
        display_patient = cursor.fetchall()
        cursor.execute("SELECT symptoms, appointment_date, appointment_time FROM Appointment WHERE clinic_id = ? AND appointment_id = ?", (clinic_id, appointment_id))
        display_appointment = cursor.fetchall()
        conn.close()
        self.view_patient_frame = Frame(self.clinic_homepage, background="white")
        self.view_patient_frame.place(height=700, width=1000, x=0, y=0)

        view_patient_topframe = Frame(self.view_patient_frame, background="cornsilk")
        view_patient_topframe.place(height=90, width=1000, x=0, y=0)

        view_patient_topframe_label = Label(view_patient_topframe, text="Patient Appointment", font=("Helvetica", 25, "bold"), background="cornsilk")
        view_patient_topframe_label.place(x=330, y=20)

        clinicbackTOHome_btn = Button(view_patient_topframe, text = " Back to homepage",background="thistle",command=lambda: self.view_patient_frame.destroy())
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        viewpatientmain_frame = Frame(self.view_patient_frame , background="cornsilk", bd=10, relief=RIDGE)
        viewpatientmain_frame.place(height=530, width=915, x=40, y=130)

        for patient in display_patient:
            patient_name = Label(viewpatientmain_frame, text="Patient Name: " + str(patient[0]), font=("Arial", 15), background="cornsilk")
            patient_name.place(x=20, y=20)
            patient_contact = Label(viewpatientmain_frame, text="Patient Contact: " + str(patient[1]), font=("Arial", 15), background="cornsilk")
            patient_contact.place(x=20, y=70)
        for appointment in display_appointment:
            symptoms = Label(viewpatientmain_frame, text="Symptoms: " + str(appointment[0]), font=("Arial", 15), background="cornsilk")
            symptoms.place(x=20, y=120)
            appointment_date = Label(viewpatientmain_frame, text="Appointment Date: " + str(appointment[1]), font=("Arial", 15), background="cornsilk")
            appointment_date.place(x=20, y=170)
            appointment_time = Label(viewpatientmain_frame, text="Appointment Time: " + str(appointment[2]), font=("Arial", 15), background="cornsilk")
            appointment_time.place(x=20, y=220)

            appointment_image = Image.open("C:/Users/MyAcer/Desktop/Software engineering/makeappointment.PNG")
            label_width, label_height = 350, 250
            appointment_image = appointment_image.resize((label_width, label_height), Image.Resampling.LANCZOS)
            appointment_image = ImageTk.PhotoImage(appointment_image)
            appointment_label = Label(viewpatientmain_frame, image=appointment_image)
            appointment_label.image = appointment_image
            appointment_label.place(height=label_height, width=label_width, x=510, y=20)

            decline_button = Button(viewpatientmain_frame, text="Decline", command=lambda: self.decline_appointment(appointment_id=appointment_id),background="thistle", borderwidth=0, font=("Arial", 13))
            decline_button.place(height=40, width=410, x=20, y=290)

            choosedoctor_button = Button(viewpatientmain_frame, text="Choose Doctor", command=lambda: self.choose_doctor(appointment_id=appointment_id),background="thistle", borderwidth=0, font=("Arial", 13))
            choosedoctor_button.place(height=40, width=410, x=450, y=290)

    def choose_doctor(self, appointment_id):
        clinic_id = self.clinic_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT doctor_id, doctor_name, doctor_qualification FROM DoctorInformation WHERE status IN (0, 1, 2) AND clinic_id = ?", (clinic_id,))
        rows = cursor.fetchall()
        doctors = {f"{row[1]} ({row[2]})": row[0] for row in rows}
        doctor_combobox = ttk.Combobox(self, values=list(doctors.keys()), width=138)
        doctor_combobox.place(x=68, y=510)

        def accept_appointment():
            selected_doctor = doctor_combobox.get()
            if selected_doctor == "":
                messagebox.showerror("Error", "Please choose a doctor.")
            else:
                doctor_id = doctors[selected_doctor]
                cursor.execute("UPDATE appointment SET doctor_id = ?, appointment_status = 1 WHERE appointment_id = ?", (doctor_id, appointment_id))
                cursor.execute("SELECT first_appointment, second_appointment, third_appointment FROM DoctorInformation WHERE doctor_id = ?", (doctor_id,))
                appointments = cursor.fetchone()
                appointment_count = sum(appointment is not None for appointment in appointments)
                if appointments[0] is None:
                    cursor.execute("UPDATE DoctorInformation SET first_appointment = ? WHERE doctor_id = ?", (appointment_id, doctor_id))
                elif appointments[1] is None:
                    cursor.execute("UPDATE DoctorInformation SET second_appointment = ? WHERE doctor_id = ?", (appointment_id, doctor_id))
                elif appointments[2] is None:
                    cursor.execute("UPDATE DoctorInformation SET third_appointment = ? WHERE doctor_id = ?", (appointment_id, doctor_id))
                cursor.execute("UPDATE DoctorInformation SET status = ? WHERE doctor_id = ?", (appointment_count + 1, doctor_id))
                conn.commit()
                messagebox.showinfo("Success", "Appointment Accepted")
                doctor_combobox.destroy()
                accept_button.destroy()
                self.view_patient_frame.destroy()

        accept_button = Button(self, text="Accept Appointment", command=accept_appointment, background="thistle", borderwidth=0, font=("Arial", 13))
        accept_button.place(height=40, width=842, x=68, y=550)


    def decline_appointment(self, appointment_id):
        reason = simpledialog.askstring("Input", "Please enter the reason for declining the appointment:", parent=self)
        if reason is not None and reason.strip() != "":
            db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(Appointment)")
            columns = [column[1] for column in cursor.fetchall()]
            if 'reason' not in columns:
                cursor.execute("ALTER TABLE Appointment ADD COLUMN reason VARCHAR(1000)")
            cursor.execute("UPDATE Appointment SET reason = ?, appointment_status = 2 WHERE appointment_id = ?", (reason, appointment_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Appointment declined")
            self.view_patient_frame.destroy()
        else:
            messagebox.showerror("Error", "Please enter a reason.")

class UploadDoctor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.upload_doctor = Frame(self, background="white")
        self.upload_doctor.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.upload_doctor , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        heading_label = Label(self.upload_doctor, text="Upload Doctor", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.upload_doctor, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        self.clinicmain_frame = Frame(self.upload_doctor , background="cornsilk")
        self.clinicmain_frame.place(height=530, width=915, x=40, y=130)

        mainframe_label = Label(self.upload_doctor, text="Doctor Information", font=("Helvetica", 25, "bold"), background="cornsilk", fg="mediumpurple")
        mainframe_label.place(x=370, y=150)

        self.doctorname_label = Label(self.upload_doctor, text="Full name :", font=(28), background="cornsilk")
        self.doctorname_label.place(x=100, y=220)
        self.doctorname_label_entry = Entry(self.upload_doctor)
        self.doctorname_label_entry.place(height=30, width=590, x=290, y=220)

        self.doctorqualification_label = Label(self.upload_doctor, text="Qualification :", font=(28), background="cornsilk")
        self.doctorqualification_label.place(x=100, y=275)
        self.doctorqualification_label_entry = Entry(self.upload_doctor)
        self.doctorqualification_label_entry.place(height=30, width=590, x=290, y=275)

        self.doctorregno_label = Label(self.upload_doctor, text="Registration number :", font=(28), background="cornsilk")
        self.doctorregno_label.place(x=100, y=330)
        self.doctorregno_label_entry = Entry(self.upload_doctor)
        self.doctorregno_label_entry.place(height=30, width=590, x=290, y=330)

        self.doctorcontact_label = Label(self.upload_doctor, text="Contact number :", font=(28), background="cornsilk")
        self.doctorcontact_label.place(x=100, y=385)
        self.doctorcontact_label_entry = Entry(self.upload_doctor)
        self.doctorcontact_label_entry.place(height=30, width=590, x=290, y=385)

        self.doctoremail_label = Label(self.upload_doctor, text="Email :", font=(28), background="cornsilk")
        self.doctoremail_label.place(x=100, y=440)
        self.doctoremail_label_entry = Entry(self.upload_doctor)
        self.doctoremail_label_entry.place(height=30, width=590, x=290, y=440)

        self.doctorusername_label = Label(self.upload_doctor, text="Username :", font=(28), background="cornsilk")
        self.doctorusername_label.place(x=100, y=495)
        self.doctorusername_label_entry = Entry(self.upload_doctor)
        self.doctorusername_label_entry.place(height=30, width=590, x=290, y=495)

        self.doctorpassword_label = Label(self.upload_doctor, text="Password :", font=(28), background="cornsilk")
        self.doctorpassword_label.place(x=100, y=550)
        self.doctorpassword_label_entry = Entry(self.upload_doctor)
        self.doctorpassword_label_entry.place(height=30, width=590, x=290, y=550)

        clinicupload_btn = Button(self.upload_doctor, text = " Upload",background="thistle",
                                  command=self.submit_doctor_registration)
        clinicupload_btn.place(height=30, width=90, x=485, y=610)

    def submit_doctor_registration(self):
        doctor_name = self.doctorname_label_entry.get()
        doctor_qualification = self.doctorqualification_label_entry.get()
        doctor_registration_no = self.doctorregno_label_entry.get()
        doctor_contact = self.doctorcontact_label_entry.get()
        doctor_email = self.doctoremail_label_entry.get()
        doctor_username = self.doctorusername_label_entry.get()
        doctor_password = self.doctorpassword_label_entry.get()
        clinic_id = self.controller.clinic_id

        dbpath = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS DoctorInformation (
                             doctor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                             doctor_name TEXT NOT NULL,
                             doctor_qualification TEXT NOT NULL,
                             doctor_registration_no INT NOT NULL,
                             doctor_contact INT NOT NULL,
                             doctor_email TEXT NOT NULL,
                             doctor_username TEXT NOT NULL,
                             doctor_password TEXT NOT NULL,
                             clinic_id INT FOREIGNKEY REFERENCES ClinicInformation(clinic_id),
                             status INT NOT NULL,
                            first_appointment INT FOREIGNKEY REFERENCES Appointment(appointment_id),
                            second_appointment INT FOREIGNKEY REFERENCES Appointment(appointment_id),
                            third_appointment INT FOREIGNKEY REFERENCES Appointment(appointment_id)
                        )
                    ''')
            
        cursor.execute('''
                        INSERT INTO DoctorInformation (doctor_name, doctor_qualification, 
                                                        doctor_registration_no, doctor_contact, 
                                                        doctor_email, doctor_username, doctor_password, 
                                                        clinic_id, status)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                       , (doctor_name, doctor_qualification, doctor_registration_no, 
                          doctor_contact, doctor_email, doctor_username, doctor_password, clinic_id , 0))
        
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Doctor uploaded successfully")
        self.controller.show_frame(ClinicHomepage)
        self.controller.clinic_id = clinic_id
        
class ManageDoctor(tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global doctor_details_tree
        self.doctor_details_tree = None
        self.clinic_id = None

        self.manage_doctor = Frame(self, background="white")
        self.manage_doctor.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.manage_doctor , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        heading_label = Label(self.manage_doctor, text="Manage Doctor", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.manage_doctor, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        dataframe = Frame(self.manage_doctor, bd=12, relief=RIDGE, background="cornsilk")
        dataframe.place(height=560, width=930, x=30, y=110)

        ####################################### Dataframe #########################################
        dataframeheading = LabelFrame(dataframe, bd=7, padx=20, relief=RIDGE, font=("Helvetica", 12, "bold"), text="Doctor Information", background="cornsilk")
        dataframeheading.place(height=245, width=885, x=10, y=7)

        self.doctorname_label = Label(dataframeheading, text="Doctor Full Name: ", font=(12), background="cornsilk", pady=9)
        self.doctorname_label.grid(row=0, column=0, sticky=W)
        self.doctorname_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorname_label_entry.grid(row=0, column=1, sticky=W)

        self.doctorqualification_label = Label(dataframeheading, text="Qualification: ", font=(12), background="cornsilk", pady=9)
        self.doctorqualification_label.grid(row=1, column=0, sticky=W)
        self.doctorqualification_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorqualification_label_entry.grid(row=1, column=1, sticky=W)

        self.doctorregno_label = Label(dataframeheading, text="Registration nummber:             ", font=(12), background="cornsilk", pady=9)
        self.doctorregno_label.grid(row=2, column=0, sticky=W)
        self.doctorregno_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorregno_label_entry.grid(row=2, column=1, sticky=W)

        self.doctorcontactno_label = Label(dataframeheading, text="Contact number: ", font=(12), background="cornsilk", pady=9)
        self.doctorcontactno_label.grid(row=3, column=0, sticky=W)
        self.doctorcontactno_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorcontactno_label_entry.grid(row=3, column=1, sticky=W)
        
        self.doctoremail_label = Label(dataframeheading, text="Email Address: ", font=(12), background="cornsilk", pady=9)
        self.doctoremail_label.grid(row=4, column=0, sticky=W)
        self.doctoremail_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctoremail_label_entry.grid(row=4, column=1, sticky=W)
        
        ########################################## Buttonframe ######################################
        buttonframe = Frame(dataframe, bd=7, relief=RIDGE, background="cornsilk")
        buttonframe.place(height=40, width=885, x=10, y=269)

        update_btn = Button(buttonframe, text="Update", background="thistle", width=47, font=("Helvetica", 11, "bold"), command=self.update_doctor)
        update_btn.grid(column=0, row=0)

        delete_btn = Button(buttonframe, text="Delete", background="thistle", width=48, font=("Helvetica", 11, "bold"), command=self.delete_doctor)
        delete_btn.grid(column=1, row=0)

        ########################################## Detailsframe ######################################
        delailsframe = Frame(dataframe, bd=7, relief=RIDGE, background="cornsilk")
        delailsframe.place(height=198, width=885, x=10, y=325)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", bg="lavender", fg="black", rowheight=15, fieldbackground="cornsilk")
        style.map("Treeview", bg=[('selected', "#F9ECE4")])

        doctordetailsframe = Frame(delailsframe)
        doctordetailsframe.place(x=8,y=5)
        treescroll = Scrollbar(doctordetailsframe)
        treescroll.pack(side=RIGHT, fill=Y)

        self.doctor_details_tree = ttk.Treeview(doctordetailsframe, yscrollcommand=treescroll.set, selectmode="extended")
        self.doctor_details_tree.pack()
        treescroll.config(command=self.doctor_details_tree.yview)

        self.doctor_details_tree['column'] = ('1', '2', '3', '4')
        self.doctor_details_tree['show'] = 'headings'

        self.doctor_details_tree.column('1', width=40, anchor='c')
        self.doctor_details_tree.column('2', width=265, anchor='c')
        self.doctor_details_tree.column('3', width=330, anchor='c')
        self.doctor_details_tree.column('4', width=205, anchor='c')

        self.doctor_details_tree.heading('1', text='ID')
        self.doctor_details_tree.heading('2', text='Full Name')
        self.doctor_details_tree.heading('3', text='Qualification')
        self.doctor_details_tree.heading('4', text='Registration Number')
    
        self.doctor_details_tree.tag_configure('odd', background="cornsilk")
        self.doctor_details_tree.tag_configure('even', background="cornsilk") 

        self.showdoctordetails()
        self.doctor_details_tree.bind('<ButtonRelease-1>', self.selectdoctor)

    def showdoctordetails(self):
        clinic_id = self.clinic_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT doctor_id, doctor_name, doctor_qualification, doctor_registration_no FROM DoctorInformation WHERE clinic_id = ?", (clinic_id,))
        rows = cursor.fetchall()
        self.doctor_details_tree.delete(*self.doctor_details_tree.get_children())
        for row in rows:
            if row[0] % 2 == 0:
                self.doctor_details_tree.insert("", tk.END, values=row, tags=('even',))
            else:
                self.doctor_details_tree.insert("", tk.END, values=row, tags=('odd',))
        conn.commit()
        conn.close()

    def selectdoctor(self, event):
        item = self.doctor_details_tree.selection()[0]
        doctor_id = self.doctor_details_tree.item(item, "values")[0]
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT doctor_name, doctor_qualification, doctor_registration_no, doctor_contact, doctor_email FROM DoctorInformation WHERE doctor_id = ?", (doctor_id,))
        row = cursor.fetchone()
        if row is not None:
            self.doctorname_label_entry.delete(0, END)
            self.doctorname_label_entry.insert(0, row[0])
            self.doctorqualification_label_entry.delete(0, END)
            self.doctorqualification_label_entry.insert(0, row[1])
            self.doctorregno_label_entry.delete(0, END)
            self.doctorregno_label_entry.insert(0, row[2])
            self.doctorcontactno_label_entry.delete(0, END)
            self.doctorcontactno_label_entry.insert(0, row[3])
            self.doctoremail_label_entry.delete(0, END)
            self.doctoremail_label_entry.insert(0, row[4])
        conn.close()

    def update_doctor(self):
        item = self.doctor_details_tree.selection()[0]
        doctor_id = self.doctor_details_tree.item(item, "values")[0]
        doctor_name = self.doctorname_label_entry.get()
        doctor_qualification = self.doctorqualification_label_entry.get()
        doctor_registration_no = self.doctorregno_label_entry.get()
        doctor_contact = self.doctorcontactno_label_entry.get()
        doctor_email = self.doctoremail_label_entry.get()
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE DoctorInformation SET doctor_name = ?, doctor_qualification = ?, doctor_registration_no = ?, doctor_contact = ?, doctor_email = ? WHERE doctor_id = ?", 
                       (doctor_name, doctor_qualification, doctor_registration_no, doctor_contact, doctor_email, doctor_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Doctor updated successfully")
        self.showdoctordetails()
        self.clearTextInput()
        self.controller.frames[ManageDoctor].update_doctordetails_tree()

    def delete_doctor(self):
        item = self.doctor_details_tree.selection()[0]
        doctor_id = self.doctor_details_tree.item(item, "values")[0]
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM DoctorInformation WHERE doctor_id = ?", (doctor_id,))
        status = cursor.fetchone()[0]
        if status != 0:
            messagebox.showerror("Delete Unsuccessful", "Doctor having appointment now")
            return
        cursor.execute("DELETE FROM DoctorInformation WHERE doctor_id = ?", (doctor_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Doctor deleted successfully")
        self.showdoctordetails()
        self.clearTextInput()

    def update_doctordetails_tree(self):
        self.doctor_details_tree.delete(*self.doctor_details_tree.get_children())
        self.showdoctordetails()

    def clearTextInput(self):
        self.doctorname_label_entry.delete(0, END)
        self.doctorqualification_label_entry.delete(0, END)
        self.doctorregno_label_entry.delete(0, END)
        self.doctorcontactno_label_entry.delete(0, END)
        self.doctoremail_label_entry.delete(0, END)

class DoctorList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.clinic_id = None

        self.doctor_list = Frame(self, background="white")
        self.doctor_list.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.doctor_list , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        heading_label = Label(self.doctor_list, text="Doctor List", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.doctor_list, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        self.refreshdoctor_btn = Button(self.doctor_list, text="Refresh", background="white", command=self.refreshdoctor, borderwidth=0)
        self.refreshdoctor_btn.place(height=20, width=60, x=850, y=100)

        self.doctorlist_canvas = Canvas(self.doctor_list, background="cornsilk")
        self.doctorlist_canvas.place(height=550, width=935, x=30, y=120)

        self.doctorlist_scrollbar = Scrollbar(self.doctor_list, orient="vertical", command=self.doctorlist_canvas.yview)
        self.doctorlist_scrollbar.place(height=550, width=20, x=965, y=120)

        self.doctorlist_canvas.configure(yscrollcommand=self.doctorlist_scrollbar.set)
        self.doctorlist_canvas.bind('<Configure>', lambda e: self.doctorlist_canvas.configure(scrollregion=self.doctorlist_canvas.bbox("all")))

        self.doctorframe_inner = Frame(self.doctorlist_canvas, background="cornsilk")
        self.doctorlist_canvas.create_window((0, 0), window=self.doctorframe_inner, anchor="nw")

        self.showdoctordetails()

    def refreshdoctor(self):
        self.doctorframe_inner.destroy()
        self.doctorframe_inner = Frame(self.doctorlist_canvas, background="cornsilk")
        self.doctorlist_canvas.create_window((0, 0), window=self.doctorframe_inner, anchor="nw")
        self.showdoctordetails()

    def showdoctordetails(self):
        clinic_id = self.clinic_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT doctor_id , doctor_name, doctor_qualification, doctor_registration_no, doctor_contact, doctor_email, status FROM DoctorInformation WHERE clinic_id = ?", (clinic_id,))
        display_doctor = cursor.fetchall()
        i=0

        def open_doctor_mainpage(doctor_id):
            def validate_password(entered_password, doctor_id=doctor_id):
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT doctor_password FROM DoctorInformation WHERE doctor_id = ?", (doctor_id,))
                print(doctor_id)
                stored_password = cursor.fetchone()

                if entered_password == "":
                    messagebox.showerror("Error", "Please enter the password")
                elif stored_password is None:
                    messagebox.showerror("Error", "Doctor ID not found")  # Handle if doctor_id is not found
                elif entered_password == stored_password[0]:
                    messagebox.showinfo("Success", "Login Successful")
                    self.controller.doctor_id = doctor_id
                    doctor_mainpage = self.controller.frames[DoctorMainpage]
                    doctor_mainpage.set_doctor_id(doctor_id) 
                    doctor_mainpage.set_doctor_name(doctor_name)
                    self.controller.show_frame(DoctorMainpage)

                else:
                    messagebox.showerror("Error", "Incorrect Password")

                conn.close()

            password_window = tk.Toplevel(self)
            password_window.title("Password Validation")

            password_label = Label(password_window, text="Enter Password:")
            password_label.pack()

            password_entry = Entry(password_window, show="*")
            password_entry.pack()

            submit_button = Button(password_window, text="Submit", command=lambda: validate_password(password_entry.get()))
            submit_button.pack()

            


        for doctor in display_doctor:
            doctor_id = doctor[0]
            doctor_frame = Frame(self.doctorframe_inner, background="cornsilk", highlightbackground="orange", highlightthickness=3, width=930, height=200)
            doctor_frame.grid(row=i, column=1, padx=1, pady=1)
            doctor_name = Label(doctor_frame, border=0, text=doctor[0], font=("Helvetica", 16, "bold"), background="cornsilk")
            doctor_name.place(x=10, y=20)
            doctor_qua = Label(doctor_frame, border=0, text=doctor[1], font=("Helvetica", 13), background="cornsilk")
            doctor_qua.place(x=10, y=60)
            doctor_regno = Label(doctor_frame, border=0, text=f"Registration No: {doctor[2]}", font=("Helvetica", 13), background="cornsilk")
            doctor_regno.place(x=10, y=90)
            doctor_contact = Label(doctor_frame, border=0, text=f"Contact: {doctor[3]}", font=("Helvetica", 13), background="cornsilk")
            doctor_contact.place(x=10, y=120)
            doctor_email = Label(doctor_frame, border=0, text=f"Email: {doctor[4]}", font=("Helvetica", 13), background="cornsilk")
            doctor_email.place(x=10, y=150)
            status_text = "BUSY" if doctor[6] == 3 else "AVAILABLE"
            status_color = "red" if doctor[6] == 3 else "green"
            doctor_status = Label(doctor_frame, border=0, text=status_text, font=("Helvetica", 14, "bold"), background="cornsilk", fg=status_color)
            doctor_status.place(x=800, y=20)
            doctor_page_button=Button(doctor_frame, text="Login", command=lambda id=doctor_id: open_doctor_mainpage(id))
            doctor_page_button.place( x=400, y=90)
            i+=1
            
            self.doctorframe_inner.update_idletasks() 
            self.doctorlist_canvas.configure(scrollregion=self.doctorlist_canvas.bbox("all"))
        conn.commit()
        conn.close()

class ClinicInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global clinic_details_tree
        self.clinic_details_tree = None
        self.clinic_id = None

        self.clinic_info = Frame(self, background="white")
        self.clinic_info.place(height=700, width=1000, x=0, y=0)

        self.clinicinfotop_frame = Frame(self.clinic_info , background="cornsilk")
        self.clinicinfotop_frame.place(height=90, width=1000, x=0, y=0)

        heading_label = Label(self.clinicinfotop_frame, text="About Us", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.clinicinfotop_frame, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        self.clinicinfomain_frame = Frame(self.clinic_info , background="cornsilk")
        self.clinicinfomain_frame.place(height=530, width=915, x=40, y=130)

        self.showclinicdetails()

    def showclinicdetails(self):
        clinic_id = self.clinic_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT clinic_name, clinic_operation_time, clinic_address, clinic_contact, clinic_description, founder_name, founder_contact, founder_email FROM ClinicInformation WHERE clinic_id = ?", (clinic_id,))
        display_clinic = cursor.fetchall()

        for clinic in display_clinic:
            clinic_name = Label(self.clinicinfomain_frame, border=0, text=clinic[0], font=("Helvetica", 30, "bold"), background="cornsilk")
            clinic_name.place(x=20, y=20)
            clinic_op_time = Label(self.clinicinfomain_frame, border=0, text=f"Operation Time: {clinic[1]}", font=("Helvetica", 15), background="cornsilk")
            clinic_op_time.place(x=20, y=140)
            clinic_address = Label(self.clinicinfomain_frame, border=0, text=f"Address: {clinic[2]}", font=("Helvetica", 15), background="cornsilk", wraplength=900, justify=LEFT)
            clinic_address.place(x=20, y=180)
            clinic_contact = Label(self.clinicinfomain_frame, border=0, text=f"Contact: {clinic[3]}", font=("Helvetica", 15), background="cornsilk")
            clinic_contact.place(x=20, y=300)
            clinic_description = Label(self.clinicinfomain_frame, border=0, text= clinic[4], font=("Helvetica", 15), background="cornsilk", wraplength=900, justify=LEFT)
            clinic_description.place(x=20, y=70)
            clinic_founder_name = Label(self.clinicinfomain_frame, border=0, text=f"Founder: {clinic[5]}", font=("Helvetica", 15), background="cornsilk")
            clinic_founder_name.place(x=20, y=410)
            clinic_founder_contact = Label(self.clinicinfomain_frame, border=0, text=f"Founder Contact: {clinic[6]}", font=("Helvetica", 15), background="cornsilk")
            clinic_founder_contact.place(x=20, y=450)
            clinic_founder_email = Label(self.clinicinfomain_frame, border=0, text=f"Founder Email: {clinic[7]}", font=("Helvetica", 15), background="cornsilk")
            clinic_founder_email.place(x=20, y=490)
            clinic_contactus_label = Label(self.clinicinfomain_frame, border=0, text="Contact Us", font=("Helvetica", 20, "bold"), background="cornsilk")
            clinic_contactus_label.place(x=20, y=260)
            clinic_founder_label = Label(self.clinicinfomain_frame, border=0, text="Founder", font=("Helvetica", 20, "bold"), background="cornsilk")
            clinic_founder_label.place(x=20, y=370)

        conn.commit()
        conn.close()

class DoctorMainpage(tk.Frame):
    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id
    
    def set_doctor_name(self, doctor_name):
        self.doctor_name = doctor_name

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.doctor_id = None
        self.doctor_name=None

    

        self.top_frame = Frame(self, background="light grey")
        self.top_frame.place(height=60, width=1300, x=1, y=1)

        log_out_btn = Button(self.top_frame, text=" Log Out", background="white", command=lambda: controller.show_frame(ClinicHomepage))
        log_out_btn.place(height=30, width=100, x=800, y=10)

        # Create a canvas that can fit the above image
        image = Image.open('C:/Users/MyAcer/Desktop/Software engineering/CAD_logo.jpg')
        label_width, label_height = 40, 40
        image = image.resize((label_width, label_height), Image.LANCZOS)  # Use Image.LANCZOS for resizing

        # Create a PhotoImage from the resized image
        image = ImageTk.PhotoImage(image)

        label = Label(self.top_frame, image=image)
        label.image = image  # Keep a reference to the image to prevent garbage collection
        label.place(height=label_height, width=label_width, x=15, y=15)

        label2 = Label(self.top_frame, text="Doctor Mainpage", font=("Helvetica", 20), background="light grey")
        label2.place(height=30, width=300, x=500, y=10)




        #right side panel
        self.right_side_panel = Frame(self, background="light grey")
        self.right_side_panel.place(height=550, width=870, x=55, y=100)

        self.lfs_right_panel =Canvas(self , bg="white")
        self.lfs_right_panel.place(height=500 , width=400 , x=75 , y=120)

        label123=Button(self.lfs_right_panel, text="Appointment", font=("Helvetica", 10),background="#FFFFFF",command=self.fetch_checkups)
        label123.pack()

        self.rhs_right_panel =Frame(self, bg="white")
        self.rhs_right_panel.place(height=500 , width=400 , x=495 , y=120)

        New_Prescription=Button(self, text="New Prescription",bg="#CBC3E3",fg="white",font="Roboto 10",command=lambda: controller.show_frame(PrescriptionPage))
        New_Prescription.place(width=380,height=50,x=510,y=150)

        View_Prescription=Button(self, text="View Prescription",bg="#CBC3E3",fg="white",font="Roboto 10",command=lambda: controller.show_frame(ViewPrescriptionsPage))
        View_Prescription.place(width=380,height=50,x=510,y=200)
        
        Manage_Prescription=Button(self, text="Manage Prescription",bg="#CBC3E3",fg="white",font="Roboto 10",command=lambda: controller.show_frame(ManagePrescriptionsPage))
        Manage_Prescription.place(width=380,height=50,x=510,y=250)

        Prescription=Label(self.rhs_right_panel, text="Prescription", font=("Helvetica", 10),background="#FFFFFF")
        Prescription.pack()
        

    def fetch_checkups(self):
        print("hello")
        doctor_name = self.doctor_name.cget("text")
        doctor_id = self.doctor_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database.db"
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM DoctorInformation WHERE doctor_id = ?", (doctor_id,))
        result = cursor.fetchone()

        if result is not None:
            cursor.execute("SELECT * FROM Appointment WHERE doctor_id = ?", (doctor_id,))
            rows = cursor.fetchall()
            
            for index, row in enumerate(rows):  # Corrected the enumerate usage
                
                cursor.execute("SELECT clinic_name FROM ClinicInformation WHERE clinic_id = ?", (row[4],))
                clinic_name = cursor.fetchone()[0]

                item = {
                    "clinic": clinic_name,
                    "time": row[2],
                    "date": row[3],
                    
                }
                print(item)

                itemframe = Frame(self.lfs_right_panel, bg="#FFFFFF", highlightbackground="black", highlightthickness=1, width=400, height=80)
                self.lfs_right_panel.create_window(330, 100 + index * 90, window=itemframe)

                clinic_label = Label(itemframe, text=f"Clinic: {clinic_name}", font=("Roboto", 14), bg="#FFFFFF")
                clinic_label.place(relx=0.05, rely=0.2, anchor="w")

                time_label = Label(itemframe, text=f"Time: {row[2]}", font=("Roboto", 14), bg="#FFFFFF")
                time_label.place(relx=0.5, rely=0.2, anchor="w")

                date_label = Label(itemframe, text=f"Date: {row[3]}", font=("Roboto", 14), bg="#FFFFFF")
                date_label.place(relx=0.05, rely=0.7, anchor="w")

                
            # Adjust the scroll region of the canvas
            self.lfs_right_panel.update_idletasks()
            self.lfs_right_panel.config(scrollregion=self.lfs_right_panel.bbox("all"))

        conn.close()


        


        
        

class PrescriptionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.prescription_frame = Frame(self, background="white")
        self.prescription_frame.place(height=700, width=1000)

        top_frame = Frame(self.prescription_frame, background="#D2E0FB")
        top_frame.place(height=60, width=1000, x=1, y=1)

        prescription_label = Label(top_frame, text="Prescription Page", font=("Helvetica", 10), background="#D2E0FB")
        prescription_label.pack()

        back_btn = Button(self.prescription_frame, text="Back", background="#F9F3CC", command=lambda: controller.show_frame(DoctorMainpage))
        back_btn.place(height=30, width=100, x=800, y=10)

        main_frame = Frame(self.prescription_frame, background="#D2E0FB")
        main_frame.place(height=550, width=900, x=55, y=100)

        title_label = Label(main_frame, text="Prescription Title: ", font=("Helvetica", 10), background="#D2E0FB")
        title_label.place(x=50, y=30)
        self.prescription_title_entry = Entry(main_frame)
        self.prescription_title_entry.place(height=30, width=500, x=250, y=30)

        content_label = Label(main_frame, text="Prescription Details: ", font=("Helvetica", 10), background="#D2E0FB")
        content_label.place(x=50, y=120)
        self.prescription_content_entry = Text(main_frame, wrap=tk.WORD)
        self.prescription_content_entry.place(height=150, width=600, x=250, y=120)

        
        self.choose_patient_button = Button(main_frame, text="Choose Patient", background="#F9F3CC", font=("Helvetica", 15), command=self.choose_patient)
        self.choose_patient_button.place(height=40, width=150, x=50, y=400)

    def choose_patient(self):
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM PatientInfo")
        patients = cursor.fetchall()

        patients_dict = {f"{pat[1]} (ID: {pat[0]})": pat[0] for pat in patients}
        patient_combobox = ttk.Combobox(self, values=list(patients_dict.keys()), width=138)
        patient_combobox.place(x=68, y=540)

        def assign_patient_to_prescription():
            selected_patient = patient_combobox.get()
            if selected_patient == "":
                messagebox.showerror("Error", "Please choose a patient.")
            else:
                patient_id = patients_dict[selected_patient]
                # Perform the prescription upload with the associated patient_id
                self.upload_prescription_with_patient(patient_id)

            patient_combobox.destroy()
            self.choose_patient_button.destroy()

        accept_button = Button(self, text="Assign Patient to Prescription", background="#F9F3CC", font=("Helvetica", 15), command=assign_patient_to_prescription)
        accept_button.place(x=68, y=560)

    def upload_prescription_with_patient(self, patient_id):
        prescription_title = self.prescription_title_entry.get()
        prescription_content = self.prescription_content_entry.get("1.0", "end-1c")
        
        if len(prescription_title) == 0 or len(prescription_content) == 0:
            messagebox.showinfo("Submit", "Both fields need to be populated, nothing saved")
            return

        # Insert prescription into the database with associated patient_id
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database.db"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute(
            "INSERT INTO PRESCRIPTIONS (Title, Content, patID) VALUES (?, ?, ?)",
            (prescription_title, prescription_content, patient_id),
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Data saved", "Prescription saved successfully!")
        self.clearPrescriptionInput()

    def clearPrescriptionInput(self):
        self.prescription_title_entry.delete(0, tk.END)
        self.prescription_content_entry.delete('1.0', tk.END)

class ViewPrescriptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.prescriptions_view_frame = Frame(self, background="white")
        self.prescriptions_view_frame.place(height=700, width=1000)

        top_frame = Frame(self.prescriptions_view_frame, background="#D2E0FB")
        top_frame.place(height=60, width=1000, x=1, y=1)

        prescriptions_label = Label(top_frame, text="View Prescriptions", font=("Helvetica", 24), background="#D2E0FB")
        prescriptions_label.pack()

        back_btn = Button(self.prescriptions_view_frame, text="Back", background="#F9F3CC", command=lambda: controller.show_frame(DoctorMainpage))
        back_btn.place(height=30, width=100, x=800, y=10)

        self.prescriptions_frame = Frame(self.prescriptions_view_frame, background="#D2E0FB")
        self.prescriptions_frame.place(height=550, width=900, x=55, y=100)

        self.load_prescriptions()

    def load_prescriptions(self):
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database.db"  # Adjust this path accordingly

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("SELECT Title, Content FROM Prescriptions")  # Query to fetch prescriptions
        prescriptions = c.fetchall()

        conn.close()

        row_count = 0
        for title, content in prescriptions:
            prescription_frame = Frame(self.prescriptions_frame, background="white", highlightbackground="black", highlightthickness=1, width=880, height=180)
            prescription_frame.grid(row=row_count, column=1, padx=1, pady=1)

            title_label = Label(prescription_frame, border=0, text=title, font=("Helvetica", 16), background="white")
            title_label.place(x=10, y=10)

            content_label = Label(prescription_frame, border=0, text=content, font=("Helvetica", 12), background="white")
            content_label.place(x=10, y=40)

            row_count += 1

class ManagePrescriptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        global tree_prescriptions  # Declare tree_prescriptions as a global variable
        tree_prescriptions = None

        self.manage_frame = Frame(self, background="white")
        self.manage_frame.place(height=700, width=1000)

        #### Top Panel #######

        self.top_frame1 = Frame(self.manage_frame, background="#D2E0FB")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        manage_label = Label(self.top_frame1, text="Manage Prescriptions Page", font=("Helvetica", 24), background="#D2E0FB")
        manage_label.pack()

        back_btn = Button(self.manage_frame, text="Back", background="#F9F3CC", command=lambda: controller.show_frame(DoctorMainpage))
        back_btn.place(height=30, width=100, x=800, y=10)

        ####### Main frame ) 

        self.frame2 = Frame(self.manage_frame, background="#D2E0FB")
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.title_label = Label(self.frame2, text="Title: ", font=(20), background="#D2E0FB")
        self.title_label.place(x=50, y=50)
        self.title_entry = Entry(self.frame2)
        self.title_entry.place(height=30, width=500, x=150, y=50)

        self.content_label = Label(self.frame2, text="Content Description: ", font=(20), background="#D2E0FB")
        self.content_label.place(x=50, y=100)
        self.content_entry = Text(self.frame2)
        self.content_entry.place(height=90, width=400, x=250, y=100)

        self.link_label = Label(self.frame2, text="Link: ", font=(20), background="#D2E0FB")
        self.link_label.place(x=50, y=200)
        self.link_entry = Entry(self.frame2)
        self.link_entry.place(height=30, width=500, x=150, y=200)

        save_btn = Button(self.frame2, text="Save", background="#F9F3CC", font=(20), command=self.save)
        save_btn.place(height=40, width=100, x=50, y=250)

        delete_btn = Button(self.frame2, text="Delete", background="#F9F3CC", font=(20), command=self.delete)
        delete_btn.place(height=40, width=100, x=150, y=250)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", bg="#D2E0FB", fg="black", rowheight=20, fieldbackground="#F9F3CC")
        style.map("Treeview", bg=[('selected', "#F9ECE4")])

        thetreeframe = Frame(self.frame2)
        thetreeframe.place(x=10, y=300)

        treescroll = Scrollbar(thetreeframe)
        treescroll.pack(side=RIGHT, fill=Y)

        tree_prescriptions = ttk.Treeview(thetreeframe, yscrollcommand=treescroll.set, selectmode="extended")
        tree_prescriptions.pack()

        treescroll.config(command=tree_prescriptions.yview)

        tree_prescriptions['column'] = ('1', '2', '3', '4')
        tree_prescriptions['show'] = 'headings'

        tree_prescriptions.column('1', width=50, anchor='c')
        tree_prescriptions.column('2', width=250, anchor='c')
        tree_prescriptions.column('3', width=300, anchor='c')
        tree_prescriptions.column('4', width=250, anchor='c')

        tree_prescriptions.heading('1', text='ID')
        tree_prescriptions.heading('2', text='Title')
        tree_prescriptions.heading('3', text='Content')
        

        tree_prescriptions.tag_configure('odd', background="#F9F3CC")
        tree_prescriptions.tag_configure('even', background="white") 
        
        self.load_prescriptions()

        tree_prescriptions.bind('<ButtonRelease-1>', self.select_item)

    def load_prescriptions(self):
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database.db"  # Adjust this path accordingly

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("SELECT Title, Content FROM PRESCRIPTIONS")  # Query to fetch prescriptions
        prescriptions = c.fetchall()

        conn.close()

        row_count = 0
        for title, content in prescriptions:
            if row_count % 2 == 0:
                tree_prescriptions.insert('', 'end', iid=row_count, values=(row_count, title, content, ''), tags=('even',))
            else:
                tree_prescriptions.insert('', 'end', iid=row_count, values=(row_count, title, content, ''), tags=('odd',))
            row_count += 1

    def update_treeview(self):
        global tree_prescriptions

        # Refresh the Treeview with the latest data from the database
        if tree_prescriptions is not None:
            tree_prescriptions.delete(*tree_prescriptions.get_children())  # Clear the existing data

        # Fetch and insert the latest data from the database
        db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("SELECT * FROM PRESCRIPTIONS")
        display_records = c.fetchall()

        conn.close()

        count = 0
        for record in display_records:
            if count % 2 == 0:
                tree_prescriptions.insert('', 'end', iid=count, values=(record[0], record[1], record[2], record[3]), tags=('even',))
            else:
                tree_prescriptions.insert('', 'end', iid=count, values=(record[0], record[1], record[2], record[3]), tags=('odd',))
            count += 1

    def save(self):
        content = self.content_entry.get("1.0", "end-1c")
        if self.title_entry.get() == "" or content == "" or self.link_entry.get() == "":
            tk.messagebox.showerror("Error", "Please do not leave any prescription details blank!")
        else:
            selected_item = tree_prescriptions.focus()
            tree_prescriptions.item(selected_item, values=(tree_prescriptions.item(selected_item)['values'][0], self.title_entry.get(), content, self.link_entry.get()))

            db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            selected_id = tree_prescriptions.item(selected_item)['values'][0]
            c.execute("UPDATE PRESCRIPTIONS SET Title=?, Content=?, Link=? WHERE ID=?", (self.title_entry.get(), content, self.link_entry.get(), selected_id))
            conn.commit()
            conn.close()

            tk.messagebox.showinfo("Success", "Prescription Updated Successfully!")
            self.clearTextInput()

    def clearTextInput(self):
        self.title_entry.delete(0, END)
        self.content_entry.delete('1.0', END)
        self.link_entry.delete(0, END)
    def delete(self):
        selected_item = tree_prescriptions.selection()
        if not selected_item:
            tk.messagebox.showinfo("Error", "Please select a prescription to delete.")
            return

        selected_item = selected_item[0]
        try:
            db_path = "C:/Users/MyAcer/Desktop/Software engineering/CAD_Database2.db"
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            selected_id = tree_prescriptions.item(selected_item)['values'][0]
            c.execute("DELETE FROM PRESCRIPTIONS WHERE ID=?", (selected_id,))
            conn.commit()
            conn.close()

            tree_prescriptions.delete(selected_item)

            tk.messagebox.showinfo("Success", "Prescription Deleted Successfully!")
            self.clearTextInput()
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def select_item(self, a):
        tree_item = tree_prescriptions.focus()
        values = tree_prescriptions.item(tree_item, 'values')
        self.title_entry.delete(0, END)
        self.title_entry.insert(0, values[1])
        self.content_entry.delete('1.0', END)
        self.content_entry.insert('1.0', values[2])
        self.link_entry.delete(0, END)
        self.link_entry.insert(0, values[3])

if __name__ == "__main__":
    app = Application()
    app.geometry('1000x700+100+0')
    app.resizable(True, True)
    app.title('Call A Doctor')
    app.mainloop()