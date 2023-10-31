import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

LARGEFONT = ("Verdana", 35)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (RegisterClinic, RegisterFounder, ClinicHomepage, DoctorList, UploadDoctor, ManageDoctor,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(RegisterClinic)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class RegisterClinic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.register_clinic = Frame(self, background="white")
        self.register_clinic.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/zhengyang/Inti/BCSCUN/Sem 4/Software Engineering/CAD_logo.jpg")
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
        self.clinictime_label = Entry(self.register_clinic)
        self.clinictime_label.place(height=30, width=350, x=100, y=335)

        self.cliniccoordinates_label = Label(self.register_clinic, text="Clinic location coordinates", font=(25), background="white")
        self.cliniccoordinates_label.place(x=100, y=390)
        self.cliniccoordinates_label = Entry(self.register_clinic)
        self.cliniccoordinates_label.place(height=30, width=350, x=100, y=415)

        self.clinicaddress_label = Label(self.register_clinic, text="Clinic address", font=(25), background="white")
        self.clinicaddress_label.place(x=100, y=470)
        self.clinicaddress_label_entry = Entry(self.register_clinic)
        self.clinicaddress_label_entry.place(height=80, width=350, x=100, y=495)

        self.cliniccontact_label = Label(self.register_clinic, text="Clinic contact number", font=(25), background="white")
        self.cliniccontact_label.place(x=570, y=310)
        self.cliniccontact_label = Entry(self.register_clinic)
        self.cliniccontact_label.place(height=30, width=350, x=570, y=335)

        self.clinicregno_label = Label(self.register_clinic, text="Clinic registration nummber", font=(25), background="white")
        self.clinicregno_label.place(x=570, y=390)
        self.clinicregno_label = Entry(self.register_clinic)
        self.clinicregno_label.place(height=30, width=350, x=570, y=415)

        self.clinicdesc_label = Label(self.register_clinic, text="Clinic description", font=(25), background="white")
        self.clinicdesc_label.place(x=570, y=470)
        self.clinicdesc_label = Entry(self.register_clinic)
        self.clinicdesc_label.place(height=80, width=350, x=570, y=495)

        nxtTOfounder_btn = Button(self.register_clinic, text = "Next", background="thistle",command=lambda: controller.show_frame(RegisterFounder))
        nxtTOfounder_btn.place(height=30, width=100,x=450, y=590)

class RegisterFounder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.register_founder = Frame(self, background="white")
        self.register_founder.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/zhengyang/Inti/BCSCUN/Sem 4/Software Engineering/CAD_logo.jpg")
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
        self.foundername_label = Entry(self.register_founder)
        self.foundername_label.place(height=30, width=350, x=330, y=275)

        self.foundercontact_label = Label(self.register_founder, text="Founder contact", font=(25), background="white")
        self.foundercontact_label.place(x=330, y=350)
        self.foundercontact_label = Entry(self.register_founder)
        self.foundercontact_label.place(height=30, width=350, x=330, y=375)

        self.founderemail_label = Label(self.register_founder, text="Founder email address", font=(25), background="white")
        self.founderemail_label.place(x=330, y=450)
        self.founderemail_label = Entry(self.register_founder)
        self.founderemail_label.place(height=30, width=350, x=330, y=475)

        nxtTOsignup_btn = Button(self.register_founder, text = "Send request to Call A Doctor",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        nxtTOsignup_btn.place(height=30, width=250,x=380, y=570)

class ClinicHomepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.clinic_homepage = Frame(self, background="white")
        self.clinic_homepage.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.clinic_homepage , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/zhengyang/Inti/BCSCUN/Sem 4/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.clinic_homepage, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = Label(self.clinic_homepage, text="Clinic Home", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicLogout_btn = Button(self.clinic_homepage, text = "Logout",background="thistle",command=lambda: controller.show_frame(RegisterClinic))
        clinicLogout_btn.place(height=30, width=60, x=910, y=25)

        self.clinicleft_frame = Frame(self.clinic_homepage , background="cornsilk")
        self.clinicleft_frame.place(height=530, width=320, x=40, y=130)

        viewDoctor_btn = Button (self.clinic_homepage , text = " Doctor List ", font=(20),background="white",command=lambda: controller.show_frame(DoctorList))
        viewDoctor_btn.place(height=70,width=200, x=100, y=200)

        uploadDoctor_btn = Button (self.clinic_homepage, text = " Upload Doctor ", font=(20),background="white", command=lambda: controller.show_frame(UploadDoctor))
        uploadDoctor_btn.place(height=70,width=200, x=100, y=350)

        manageDoctor_btn = Button (self.clinic_homepage , text = " Manage Doctor ", font=(20),background="white", command=lambda: controller.show_frame(ManageDoctor))
        manageDoctor_btn.place(height=70,width=200, x=100, y=500)

        self.clinicright_frame = Frame(self.clinic_homepage , background="cornsilk")
        self.clinicright_frame.place(height=530, width=540, x=410, y=130)

        self.patient_label = Label(self.clinic_homepage, text="Patient", font=(25), background="white")
        self.patient_label.place(height=70,width=480, x=440, y=160)       

class DoctorList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.doctor_list = Frame(self, background="white")
        self.doctor_list.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.doctor_list , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/zhengyang/Inti/BCSCUN/Sem 4/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.doctor_list, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = Label(self.doctor_list, text="Doctor List", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.doctor_list, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

class UploadDoctor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.upload_doctor = Frame(self, background="white")
        self.upload_doctor.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.upload_doctor , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/zhengyang/Inti/BCSCUN/Sem 4/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.upload_doctor, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = Label(self.upload_doctor, text="Uplaod Doctor", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.upload_doctor, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        self.clinicmain_frame = Frame(self.upload_doctor , background="cornsilk")
        self.clinicmain_frame.place(height=530, width=915, x=40, y=130)

        mainframe_label = Label(self.upload_doctor, text="Doctor Information", font=("Helvetica", 25, "bold"), background="cornsilk", fg="mediumpurple")
        mainframe_label.place(x=370, y=150)

        self.doctorname_label = Label(self.upload_doctor, text="Full name :", font=(28), background="cornsilk")
        self.doctorname_label.place(x=100, y=220)
        self.doctorname_label = Entry(self.upload_doctor)
        self.doctorname_label.place(height=30, width=590, x=290, y=220)

        self.doctorqualification_label = Label(self.upload_doctor, text="Qualification :", font=(28), background="cornsilk")
        self.doctorqualification_label.place(x=100, y=275)
        self.doctorqualification_label = Entry(self.upload_doctor)
        self.doctorqualification_label.place(height=30, width=590, x=290, y=275)

        self.doctorregno_label = Label(self.upload_doctor, text="Registration number :", font=(28), background="cornsilk")
        self.doctorregno_label.place(x=100, y=330)
        self.doctorregno_label = Entry(self.upload_doctor)
        self.doctorregno_label.place(height=30, width=590, x=290, y=330)

        self.doctorcontact_label = Label(self.upload_doctor, text="Contact number :", font=(28), background="cornsilk")
        self.doctorcontact_label.place(x=100, y=385)
        self.doctorcontact_label = Entry(self.upload_doctor)
        self.doctorcontact_label.place(height=30, width=590, x=290, y=385)

        self.doctoremail_label = Label(self.upload_doctor, text="Email :", font=(28), background="cornsilk")
        self.doctoremail_label.place(x=100, y=440)
        self.doctoremail_label = Entry(self.upload_doctor)
        self.doctoremail_label.place(height=30, width=590, x=290, y=440)

        self.doctorusername_label = Label(self.upload_doctor, text="Username :", font=(28), background="cornsilk")
        self.doctorusername_label.place(x=100, y=495)
        self.doctorusername_label = Entry(self.upload_doctor)
        self.doctorusername_label.place(height=30, width=590, x=290, y=495)

        self.doctorpassword_label = Label(self.upload_doctor, text="Password :", font=(28), background="cornsilk")
        self.doctorpassword_label.place(x=100, y=550)
        self.doctorpassword_label = Entry(self.upload_doctor)
        self.doctorpassword_label.place(height=30, width=590, x=290, y=550)

        clinicupload_btn = Button(self.upload_doctor, text = " Upload",background="thistle",command=lambda: controller.show_frame(DoctorList))
        clinicupload_btn.place(height=30, width=90, x=485, y=610)



class ManageDoctor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.manage_doctor = Frame(self, background="white")
        self.manage_doctor.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.manage_doctor , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/zhengyang/Inti/BCSCUN/Sem 4/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.manage_doctor, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = Label(self.manage_doctor, text="Manage Doctor", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.manage_doctor, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

if __name__ == "__main__":
    app = Application()
    app.geometry('1000x700+100+0')
    app.resizable(True, True)
    app.title('Call A Doctor')
    app.mainloop()

