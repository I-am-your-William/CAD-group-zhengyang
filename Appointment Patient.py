import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import StringVar, messagebox
from tkinter import messagebox
import sqlite3

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (ViewAllClinicPage, HomePage ) :
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.home_frame = Frame(self, background="#D2E0FB")
        self.home_frame.place(height=700, width=1000)

        #### Top Panel #######
        self.top_frame1 = Frame(self.home_frame, background="#D2E0FB")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        viewclinicbtn = Button(self.top_frame1, text="View Clinic", command=lambda: controller.show_frame(ViewAllClinicPage),background="#F9F3CC")
        viewclinicbtn.place(height=30, width=100, x=100, y=10)


class ViewAllClinicPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.clinicView_frame = Frame(self, background="white")
        self.clinicView_frame.place(height=700, width=1000)

        #### Top Panel #######
        self.top_frame1 = Frame(self.clinicView_frame , background="#D2E0FB")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        clinicView_label  = Label(self.top_frame1 ,  text="View Clinic Page", font=("Helvetica", 24),background = "#D2E0FB")
        clinicView_label.pack()

        back_btn = Button(self, text="Back", background="#F9F3CC", command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100, x=800, y=10)

        ####### Main frame #####
        self.frame2 = Frame(self.clinicView_frame, background="#D2E0FB")
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.viewClinic_canvas = Canvas(self.frame2, background="#F9F3CC")
        self.viewClinic_canvas.place(height=550, width=900, x=0, y=0)

        scrollbar = Scrollbar(self.frame2, orient=VERTICAL, command=self.viewClinic_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.viewClinic_canvas.configure(yscrollcommand=scrollbar.set)
        self.viewClinic_canvas.bind('<Configure>', lambda _: self.viewClinic_canvas.configure(scrollregion=self.viewClinic_canvas.bbox("all")))

        frame_inner = Frame(self.viewClinic_canvas)
        self.viewClinic_canvas.create_window((0, 0), window=frame_inner, anchor="nw")

        self.load_clinic(frame_inner)

    def load_clinic(self, frame_inner):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)  # Connect to the existing database
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ClinicInformation WHERE status=1")
        displayrecord = self.c.fetchall()

        i = 0
        for _ in displayrecord:
            clinic_frame = Frame(frame_inner, background="white", highlightbackground="black", highlightthickness=1, width=900,height=100)
            clinic_frame.grid(row=i, column=1, padx=1, pady=1)
            clinic_name = Label(clinic_frame, text=displayrecord[i][1], font=("Helvetica", 16), background="white")
            clinic_name.place(x=10, y=20)
            clinic_location = Label(clinic_frame, text="Location : " + displayrecord[i][4], font=("Helvetica", 10), background="white")
            clinic_location.place(x=10, y=50)
            clinic_operation_hour = Label(clinic_frame, text="Operation Hour : " + displayrecord[i][5], font=("Helvetica", 10), background="white")
            clinic_operation_hour.place(x=10, y=70)
            clinic_contact = Label(clinic_frame, text="Contact : " + str(displayrecord[i][6]), font=("Helvetica", 10), background="white")
            clinic_contact.place(x=10, y=90)
            clinic_button = Button(clinic_frame, text="More Information", command=lambda i=i: self.more_information(clinic_id=displayrecord[i][0]),background="#F9F3CC")
            clinic_button.place(height=30, width=150, x=700, y=55)
            i += 1

        self.conn.close()

    def more_information(self, clinic_id):
        #hardcoded pat_id for testing
        patID =  1

        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ClinicInformation WHERE clinic_id=?", (clinic_id,))
        selected_record = self.c.fetchone()
        self.conn.close()

        more_info_frame = tk.Frame(self.clinicView_frame, background="#F9F3CC")
        more_info_frame.place(height=640, width=1000, x=0, y=60)

        left_panel1 = Frame(more_info_frame, background="white", highlightbackground="black", highlightthickness=1)
        left_panel1.place(height=500, width=550, x=30, y=100)

        back_button = tk.Button(more_info_frame, text="Back to Clinic List", command=lambda: more_info_frame.destroy())
        back_button.place(height=30, width=130, x=30, y=30)

        clinic_name = tk.Label(more_info_frame, text=selected_record[1], font=("Helvetica", 25), background="#F9F3CC")
        clinic_name.place(height=40, width=300, x=350, y=30)

        clinic_info = tk.Label(left_panel1, text="Clinic Information", font=("Helvetica", 20), background="white")
        clinic_info.pack(pady=20)
        clinic_operationTime = tk.Label(left_panel1, text="Operation Time: " + selected_record[2], font=("Helvetica", 10), background="white")
        clinic_operationTime.pack(pady=1, anchor="w")
        clinic_phoneNumber = tk.Label(left_panel1, text="Phone Number: " + selected_record[5], font=("Helvetica", 10), background="white")
        clinic_phoneNumber.pack(pady=1, anchor="w")
        clinic_location = tk.Label(left_panel1, text="Location: " + selected_record[4], font=("Helvetica", 10), background="white", wraplength=400)
        clinic_location.pack(pady=1, padx=1, anchor="w")
        clinic_description = tk.Label(left_panel1, text="Description: " + selected_record[7], font=("Helvetica", 10), background="white")
        clinic_description.pack(pady=1, anchor="w")

        right_panel1 = Frame(more_info_frame, background="white", highlightbackground="black", highlightthickness=1)
        right_panel1.place(height=500, width=400, x=600, y=100)

        bookAppointment = tk.Label(right_panel1, text="Book Appointment", font=("Helvetica", 20), background="white")
        bookAppointment.pack(pady=20)

        symptoms = tk.Label(right_panel1, text="Symptoms: ", font=("Helvetica", 10), background="white")
        symptoms.place(height=30, width=100, x=10, y=140)
        symptoms_entry = tk.Entry(right_panel1)
        symptoms_entry.place(height=30, width=200, x=120, y=140)

        appointment_time = tk.Label(right_panel1, text="Time: ", font=("Helvetica", 10), background="white")
        appointment_time.place(height=30, width=100, x=10, y=180)
        appointment_time_entry = tk.Entry(right_panel1)
        appointment_time_entry.place(height=30, width=200, x=120, y=180)

        appointment_date = tk.Label(right_panel1, text="Date: ", font=("Helvetica", 10), background="white")
        appointment_date.place(height=30, width=100, x=10, y=100)
        appointment_date_entry = tk.Entry(right_panel1)
        appointment_date_entry.place(height=30, width=200, x=120, y=100)

        book_button = tk.Button(right_panel1, text="Book", command=lambda: self.book_appointment(clinic_id, patID, symptoms_entry.get(), appointment_time_entry.get(), appointment_date_entry.get()))
        book_button.place(height=30, width=100, x=150, y=220)

    def book_appointment(self, clinic_id, patID, symptoms, appointment_time, appointment_date):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ClinicInformation WHERE clinic_id=?", (clinic_id,))

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS Appointment (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                symptoms TEXT NOT NULL,
                appointment_time TEXT NOT NULL,
                appointment_date TEXT NOT NULL,
                clinic_id NOT NULL REFERENCES ClinicInformation(clinic_id),
                patID NOT NULL REFERENCES PatientInfo(patID),
                appointment_status INT NOT NULL 
            )



        ''')

        self.c.execute("INSERT INTO Appointment (patID, clinic_id, symptoms, appointment_time, appointment_date,appointment_status) VALUES (?, ?, ?, ?, ?, ?)", (patID, clinic_id, symptoms, appointment_time, appointment_date, 0))
        self.conn.commit()
        self.conn.close()

        messagebox.showinfo("Success", "Appointment booked successfully!")

        


if __name__ == "__main__":
        app = Application()
        app.geometry('1000x700')
        app.resizable(True, True)
        app.title('Call A Doctor')

        app.mainloop()




       


