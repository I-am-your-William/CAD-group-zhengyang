import tkinter as tk
from tkinter import *
from tkinter import ttk
import  tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3
from contextlib import closing
import webbrowser

LARGEFONT = ("Verdana", 35)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, UploadPage, ManagePage, ClinicRequestPage, ViewAllClinicPage, ViewTipsPage,LoginAdmin ) :
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginAdmin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.login_admin = tk.Frame(self, background="white")
        self.login_admin.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(self.login_admin, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = tk.Label(self.login_admin, text="Admin Login", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=416, y=160)

        self.adminloginusername_label = tk.Label(self.login_admin, text="Username", font=(25), background="white")
        self.adminloginusername_label.place(x=330, y=250)

        self.adminloginusername_entry = tk.Entry(self.login_admin)
        self.adminloginusername_entry.place(height=30, width=350, x=330, y=275)

        self.adminloginpassword_label = tk.Label(self.login_admin, text="Password", font=(25), background="white")
        self.adminloginpassword_label.place(x=330, y=350)

        self.adminloginpassword_entry = tk.Entry(self.login_admin)
        self.adminloginpassword_entry.place(height=30, width=350, x=330, y=375)

        login_btn = tk.Button(self.login_admin, text="Login", background="thistle", command=self.login)
        login_btn.place(height=30, width=100, x=447, y=470)

    def login(self):
        if self.adminloginusername_entry.get() == "" or self.adminloginpassword_entry.get() == "":
            tkinter.messagebox.showerror("Error", "Please do not leave any fields blank!")
        else:
            if self.adminloginusername_entry.get() == "admin12345" and self.adminloginpassword_entry.get() == "admin12345":
                tkinter.messagebox.showinfo("Success", "Login Successful!")
                self.controller.show_frame(HomePage)
            else:
                tkinter.messagebox.showerror("Error", "Invalid Username or Password!")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ###########Top Panel #############

        home_page = Frame(self ,background="white")
        home_page.place(height=700, width=1000, x=0, y=0)

        self.top_frame = Frame(home_page, background="#D2E0FB")
        self.top_frame.place(height=60, width=1000, x=1, y=1)

        heading_label = Label(self.top_frame, text="Call A Doctor Admin Home Page", font=("Helvetica", 24), background="#D2E0FB")
        heading_label.pack()

        log_out_btn = Button(self.top_frame, text="Log Out", background="#F9F3CC", command=lambda: controller.show_frame(LoginAdmin))
        log_out_btn.place(height=30, width=100, x=800, y=10)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 40, 40
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS for resizing

        # Create a PhotoImage from the resized image
        image = ImageTk.PhotoImage(image)

        label = Label(self.top_frame, image=image)
        label.image = image  # Keep a reference to the image to prevent garbage collection
        label.place(height=label_height, width=label_width, x=30, y=10)

        #######left side panel########
        self.left_side_panel = Frame(home_page , background="#D2E0FB")
        self.left_side_panel.place(height=550, width=300, x=55, y=100)

        view_clinic_btn = Button (self.left_side_panel , text = " View All Clinic ", font=(20),background="#F9F3CC",command=lambda: controller.show_frame(ViewAllClinicPage))
        view_clinic_btn.place(height=70,width=200, x=50, y=40)

        upload_tip_btn = Button (self.left_side_panel, text = " Upload Tips ", font=(20),background="#F9F3CC", command=lambda: controller.show_frame(UploadPage))
        upload_tip_btn.place(height=70,width=200, x=50, y=180)

        manage_tip_btn = Button (self.left_side_panel , text = " Manage Tips ", font=(20),background="#F9F3CC", command=lambda: controller.show_frame(ManagePage))
        manage_tip_btn.place(height=70,width=200, x=50, y=330)

        view_all_tips_btn = Button (self.left_side_panel , text = " View All Tips ", font=(20),background="#F9F3CC", command=lambda: controller.show_frame(ViewTipsPage))
        view_all_tips_btn.place(height=70,width=200, x=50, y=470)

        #right side panel
        self.right_side_panel = Frame(home_page , background="#D2E0FB")
        self.right_side_panel.place(height=550, width=550, x=390, y=100)

        request_btn = Button (self.right_side_panel, text = " Clinic Request  ", font=(20), background="#F9F3CC", command=lambda: controller.show_frame(ClinicRequestPage) )
        request_btn.place(height=70, width=450, x=50, y=50)

        right_frame = Frame(self.right_side_panel, background="#F9F3CC")
        right_frame.place(height=350, width=450, x=50, y=150)

        self.request_canvas = Canvas(right_frame, background="#F9F3CC")
        self.request_canvas.place(height=350, width=450, x=0, y=0)

        scrollbar = Scrollbar(right_frame, orient=VERTICAL, command=self.request_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.request_canvas.configure(yscrollcommand=scrollbar.set)
        self.request_canvas.bind('<Configure>', lambda e: self.request_canvas.configure(scrollregion=self.request_canvas.bbox("all")))

        frame_inner = Frame(self.request_canvas, background="lightgrey")

        self.request_canvas.create_window((0, 0), window=frame_inner, anchor="nw")

        #Refresh Button
        refresh_btnimage = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/refresh btn.png")
        refresh_btnimage = refresh_btnimage.resize((20, 20), Image.ANTIALIAS)
        refresh_btnimage = ImageTk.PhotoImage(refresh_btnimage)

        refresh_btn = Button(self.right_side_panel, image=refresh_btnimage, background="white", command=self.refresh_request)
        refresh_btn.image = refresh_btnimage
        refresh_btn.place(x=470, y=120)

        self.load_request(frame_inner)

    def load_request(self, frame_inner):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ClinicInformation WHERE status=0")
        displayrecord = self.c.fetchall()

        i = 0
        for _ in displayrecord:
            request_frame = Frame(frame_inner, background="white", highlightbackground="black", highlightthickness=1, width=430,height=80)
            request_frame.grid(row=i, column=1, padx=1, pady=1)
            request_name = Label(request_frame, text=displayrecord[i][1], font=("Helvetica", 12),background="white")
            request_name.place(x=10, y=10)
            request_status = Label(request_frame, text="Status : Pending", font=("Helvetica", 12),background="white")
            request_status.place(x=10, y=40)

            i += 1

    # Refresh the request list

    def refresh_request(self):
        for widget in self.request_canvas.winfo_children():
            widget.destroy()

        # Fetch and display the latest data
        frame_inner = Frame(self.request_canvas)
        self.request_canvas.create_window((0, 0), window=frame_inner, anchor="nw")
        self.load_request(frame_inner)

        # Reset the scrollregion of the Canvas
        self.request_canvas.update_idletasks()


    def log_out(self):
         self.controller.destroy()
         

class UploadPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        self.upload_frame = Frame(self, background="white")
        self.upload_frame.place(height=700, width=1000)
        

        #### Top Panel #######

        self.top_frame1 = Frame(self.upload_frame , background="#D2E0FB")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        upload_label  = Label(self.top_frame1 ,  text="Upload Tips Page", font=("Helvetica", 24),background = "#D2E0FB")
        upload_label .pack()

        back_btn = Button(self, text = "Back",background="#F9F3CC",command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100,x=800, y=10)

        #### Main Frame ######

        self.frame2 = Frame(self.upload_frame , background = "#D2E0FB" )
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.title_label = Label(self.frame2, text = "Tilte : ", font=(20),background = "#D2E0FB")
        self.title_label.place(x=50, y=30)
        self.title_entry = Entry(self.frame2)
        self.title_entry.place(height=30,width=500, x=150, y=30)

        self.content_label = Label(self.frame2, text = "Content Description : ", font=(20),background = "#D2E0FB")
        self.content_label.place(x=50, y=120)
        self.content_entry = Text(self.frame2)
        self.content_entry.place(height=90,width=600, x=50, y=150)

        self.link_label = Label(self.frame2, text = "Link : ", font=(20),background = "#D2E0FB")
        self.link_label.place(x=50, y=300)
        self.link_entry = Entry(self.frame2)
        self.link_entry.place(height=30,width=500, x=150, y=300)

        upload_btn = Button(self.frame2, text = "Upload",background="#F9F3CC", font=(20),command=self.upload)
        upload_btn.place(height=50, width=100,x=50, y=400)

    def upload(self):
        # Extract the content from the Text widget
        self.title_entry_submit = self.title_entry.get()
        self.content_entry_submit = self.content_entry.get("1.0", "end-1c")  # Retrieve the entire content
        self.link_entry_submit = self.link_entry.get()

        # Making sure all three fields are populated before submitting to the database
        if (
            len(self.title_entry.get()) == 0
            or len(self.content_entry_submit) == 0  # Use the extracted content
            or len(self.link_entry.get()) == 0
        ):
            tkinter.messagebox.showinfo("Submit", "All fields need to be populated, nothing saved")
        else:
            # Use the existing database file path
            db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"

            self.conn = sqlite3.connect(db_path)  # Connect to the existing database
            self.c = self.conn.cursor()  # Create a cursor

            # Check if the "TIPS" table exists, and if not, create it
            self.c.execute("""
                CREATE TABLE IF NOT EXISTS TIPS (
                    Post_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    TITLE VARCHAR(100) NOT NULL,
                    CONTENT VARCHAR(1000) NOT NULL,
                    LINK VARCHAR(100) NOT NULL
                )
            """)

            # Continue with inserting the data
            self.c.execute(
                "INSERT INTO TIPS (TITLE, CONTENT, LINK) VALUES(?,?,?)",
                (self.title_entry_submit, self.content_entry_submit, self.link_entry_submit),
            )
            new_post_id = self.c.lastrowid
            self.conn.commit()
            self.conn.close()

            tkinter.messagebox.showinfo("Data saved", "Data saved successfully!")
            self.clearTextInput()

            # Refresh the treeview in the ManagePage
            self.controller.frames[ManagePage].update_treeview()

            

            # Method to clear out what was submitted so the data can't be entered twice in error.
    def clearTextInput(self):
        self.title_entry.delete('0', END)
        self.content_entry.delete('1.0', END)
        self.link_entry.delete('0', END)

    def refreshtree(self):
        self.upload_frame.destroy() #closes window
        self.master() #reopens window    
  

class ManagePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        global tree_tips  # Declare tree_tips as a global variable
        tree_tips = None

        self.manage_frame = Frame(self, background="white")
        self.manage_frame.place(height=700, width=1000)

        #### Top Panel #######

        self.top_frame1 = Frame(self.manage_frame , background="#D2E0FB")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        manage_label  = Label(self.top_frame1 ,  text="Manage Tips Page", font=("Helvetica", 24),background = "#D2E0FB")
        manage_label .pack()

        back_btn = Button(self, text = "Back",background="#F9F3CC",command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100,x=800, y=10)

        ####### Main frame ) 

        self.frame2 = Frame(self.manage_frame , background = "#D2E0FB" )
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.title_label = Label(self.frame2, text = "Tilte : ", font=(20),background ="#D2E0FB")
        self.title_label.place(x=50, y=50)
        self.title_entry = Entry(self.frame2)
        self.title_entry.place(height=30,width=500, x=150, y=50)

        self.content_label = Label(self.frame2, text = "Content Description : ", font=(20),background = "#D2E0FB")
        self.content_label.place(x=50, y=100)
        self.content_entry = Text(self.frame2)
        self.content_entry.place(height=90,width=400, x=250, y=100)

        self.link_label = Label(self.frame2, text = "Link : ", font=(20),background ="#D2E0FB")
        self.link_label.place(x=50, y=200)
        self.link_entry = Entry(self.frame2)
        self.link_entry.place(height=30,width=500, x=150, y=200)

        save_btn = Button(self.frame2, text = "Save",background="#F9F3CC", font=(20),command=self.save)
        save_btn.place(height=40, width=100,x=50, y=250)

        delete_btn = Button(self.frame2, text = "Delete",background="#F9F3CC", font=(20),command=self.delete)
        delete_btn.place(height=40, width=100,x=150, y=250)


        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", bg="#D2E0FB", fg="black", rowheight=20, fieldbackground="#F9F3CC")
        style.map("Treeview", bg=[('selected', "#F9ECE4")])


        thetreeframe = Frame(self.frame2)
        thetreeframe.place(x=10,y=300)

        treescroll = Scrollbar(thetreeframe)
        treescroll.pack(side=RIGHT, fill=Y)

        tree_tips = ttk.Treeview(thetreeframe, yscrollcommand=treescroll.set, selectmode="extended")
        tree_tips.pack()

        treescroll.config(command=tree_tips.yview)

        tree_tips['column'] = ('1', '2', '3', '4')
        tree_tips['show'] = 'headings'

        tree_tips.column('1', width=50, anchor='c')
        tree_tips.column('2', width=250, anchor='c')
        tree_tips.column('3', width=300, anchor='c')
        tree_tips.column('4', width=250, anchor='c')

        tree_tips.heading('1', text='ID')
        tree_tips.heading('2', text='Title')
        tree_tips.heading('3', text='Content')
        tree_tips.heading('4', text='Link')
    
        tree_tips.tag_configure('odd', background="#F9F3CC")
        tree_tips.tag_configure('even', background="white") 
        
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"

        self.conn = sqlite3.connect(db_path)  # Connect to the existing database
        self.c = self.conn.cursor()  # Create a cursor

        # Check if the "TIPS" table exists, and if not, create it
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS TIPS (
                Post_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TITLE VARCHAR(100) NOT NULL,
                CONTENT VARCHAR(1000) NOT NULL,
                LINK VARCHAR(100) NOT NULL
            )
        """)

        # Continue with executing the SELECT statement
        self.c.execute("SELECT * FROM TIPS")
        displayrecord = self.c.fetchall()

        global count 
        count = 0
        for all in displayrecord: 
            if count % 2 == 0:  
                tree_tips.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3]), tags=('even',))
            else:
                tree_tips.insert('', 'end', iid = count, values = (all[0], all[1], all[2],all[3]), tags=('odd',))
            count += 1

        tree_tips.bind('<ButtonRelease-1>', self.select_item)


    def update_treeview(self):
        global tree_tips  # Use the global variable tree_tips

        # Refresh the Treeview with the latest data from the database
        if tree_tips is not None:
            tree_tips.delete(*tree_tips.get_children())  # Clear the existing data

        # Fetch and insert the latest data from the database
         
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"

        self.conn = sqlite3.connect(db_path)  # Connect to the existing database
        self.c = self.conn.cursor()  # Create a cursor

        # Check if the "TIPS" table exists, and if not, create it
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS TIPS (
                Post_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TITLE VARCHAR(100) NOT NULL,
                CONTENT VARCHAR(1000) NOT NULL,
                LINK VARCHAR(100) NOT NULL
            )
        """)
        self.c.execute("SELECT * FROM TIPS")
        displayrecord = self.c.fetchall()

        global count
        count = 0
        for all in displayrecord:
            if count % 2 == 0:
                tree_tips.insert('', 'end', iid=count, values=(all[0], all[1], all[2], all[3]), tags=('even',))
            else:
                tree_tips.insert('', 'end', iid=count, values=(all[0], all[1], all[2], all[3]), tags=('odd',))
            count += 1
        
    
    def save(self):
        self.content_entry_submit = self.content_entry.get("1.0", "end-1c") 
        if self.title_entry.get() == "" or self.content_entry_submit == "" or self.link_entry.get() == "":
            tkinter.messagebox.showerror("Error", "Please do not leave any event details blank!")
        else:
            select = tree_tips.focus()
            # Update the Treeview with new data
            tree_tips.item(select, values=(tree_tips.item(select)['values'][0], self.title_entry.get(), self.content_entry_submit, self.link_entry.get()))
            
            # Update the database
            dbpath = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
            self.conn = sqlite3.connect(dbpath)
            self.c = self.conn.cursor()
            self.c.execute("UPDATE TIPS SET TITLE=?, CONTENT=?, LINK=? WHERE Post_ID=?", (self.title_entry.get(), self.content_entry_submit, self.link_entry.get(), tree_tips.item(select)['values'][0]))
            self.conn.commit()
            self.conn.close()
            tkinter.messagebox.showinfo("Success", "Record Updated Successfully!")
            self.clearTextInput()

 
    

    def clearTextInput(self):
        self.title_entry.delete('0', END)
        self.content_entry.delete('1.0', END)
        self.link_entry.delete('0', END)    

    def delete(self):
        selected_item = tree_tips.selection()
        if not selected_item:
            tkinter.messagebox.showinfo("Error", "Please select a record to delete.")
            return

        selected_item = selected_item[0]
        try:
            self.conn = sqlite3.connect("CAD_Database.db")
            self.c = self.conn.cursor()

            # Get the Post_ID of the selected item
            post_id = tree_tips.item(selected_item)['values'][0]

            # Delete the record from the database
            db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            self.c.execute("DELETE FROM TIPS WHERE Post_ID=?", (post_id,))
            self.conn.commit()
            self.conn.close()

            # Delete the item from the Treeview
            tree_tips.delete(selected_item)

            tkinter.messagebox.showinfo("Success", "Record Deleted Successfully!")
            self.clearTextInput()
        except Exception as e:
            tkinter.messagebox.showerror("Error", str(e))


    def select_item(self, a):
        tree_item = tree_tips.focus()
        values = tree_tips.item(tree_item, 'values')
        self.title_entry.delete(0, END)
        self.title_entry.insert(0, values[1])
        self.content_entry.delete('1.0', END)
        self.content_entry.insert('1.0', values[2])
        self.link_entry.delete(0, END)
        self.link_entry.insert(0, values[3])

        
class ClinicRequestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.request_frame = Frame(self, background="white")
        self.request_frame.place(height=700, width=1000)

        #### Top Panel #######

        self.top_frame2 = Frame(self.request_frame , background="#D2E0FB")
        self.top_frame2.place(height=60, width=1000, x=1, y=1)

        request_label  = Label(self.top_frame2 ,  text="Clinic Request Page", font=("Helvetica", 24),background = "#D2E0FB")
        request_label .pack()

        back_btn = Button(self, text="Back", background="#F9F3CC", command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100, x=800, y=10)

        refresh_btn = Button(self, text="Refresh", background="#F9F3CC", command=self.refresh_request)
        refresh_btn.place(height=30, width=100, x=100, y=10)

        #############

        self.frame2 = Frame(self.request_frame, background="#D2E0FB")
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.request_canvas = Canvas(self.frame2, background="#F9F3CC")
        self.request_canvas.place(height=550, width=900, x=0, y=0)

        scrollbar = Scrollbar(self.frame2, orient=VERTICAL, command=self.request_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.request_canvas.configure(yscrollcommand=scrollbar.set)
        self.request_canvas.bind('<Configure>', lambda e: self.request_canvas.configure(scrollregion=self.request_canvas.bbox("all")))

        frame_inner = Frame(self.request_canvas, background="#D2E0FB")
        self.request_canvas.create_window((0, 0), window=frame_inner, anchor="nw")

        self.load_request(frame_inner)

    def load_request(self, frame_inner):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)  # Connect to the existing database
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ClinicInformation WHERE status=0")
        displayrecord = self.c.fetchall()

        i = 0
        for _ in displayrecord:
            request_frame = Frame(frame_inner, background="white", highlightbackground="black", highlightthickness=1, width=900,height=100)
            request_frame.grid(row=i, column=1, padx=1, pady=1)
            request_name = Label(request_frame, text=displayrecord[i][1], font=("Helvetica", 16), background="white")
            request_name.place(x=10, y=20)
            request_location = Label(request_frame, text="Location : " + displayrecord[i][4], font=("Helvetica", 10), background="white")
            request_location.place(x=10, y=50)
            
            request_button = Button(request_frame, text="More Information",background="#F9F3CC", command=lambda i=i: self.accept_request(clinic_id=displayrecord[i][0]))
            request_button.place(height=30, width=150, x=700, y=35)

            i += 1

        self.conn.close()
    
    def refresh_request(self):
        for widget in self.request_canvas.winfo_children():
            widget.destroy()

        # Fetch and display the latest data
        frame_inner = Frame(self.request_canvas)
        self.request_canvas.create_window((0, 0), window=frame_inner, anchor="nw")
        self.load_request(frame_inner)

        # Reset the scrollregion of the Canvas
        self.request_canvas.update_idletasks()  # Ensure all widgets are updated
        self.request_canvas.config(scrollregion=self.request_canvas.bbox("all"))

    def accept_request(self, clinic_id):
        # Fetch the information for the selected user_id
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ClinicInformation WHERE clinic_id=?", (clinic_id,))
        selected_record = self.c.fetchone()
        self.conn.close()

        # Create a new frame to display additional information
        more_info_frame = tk.Frame(self.request_frame, background="#F9F3CC")
        more_info_frame.place(height=640, width=1000, x=0, y=60)

        left_panel1 = Frame(more_info_frame, background="white", highlightbackground="black", highlightthickness=1)
        left_panel1.place(height=500, width=550, x=30, y=100)    

        right_panel1 = Frame(more_info_frame, background="white", highlightbackground="black", highlightthickness=1)
        right_panel1.place(height=250, width=350, x=610, y=100)

        back_button = tk.Button(more_info_frame, text="Back to Clinic Request", command=lambda: more_info_frame.destroy())
        back_button.place(height=30, width=130, x=30, y=30)
        

        # Define the callback function
        def callback(url):
            webbrowser.open_new(url)

        #Right Panel

        first_label = tk.Label(right_panel1, text="1. Click on this Link below ", font=("Helvetica", 10),background="white")
        first_label.place(height=30, width=150, x=20, y=20)
        link = tk.Label(right_panel1, text="https://meritsmmc.moh.gov.my/search", font=("Helvetica", 10),background="white",fg="blue")
        link.place(height=30, width=250, x=20, y=40)
        link.bind("<Button-1>", lambda e:callback("https://meritsmmc.moh.gov.my/search"))
        link.config(cursor="hand2")
        second_label = tk.Label(right_panel1, text="2. Search the clinic name on the website ", font=("Helvetica", 10),background="white")
        second_label.place(height=30, width=240, x=20, y=70)
        third_label = tk.Label(right_panel1, text=("3. Check and verify the founder name \n" + "and registration number of the clinic " ), font=("Helvetica", 10),background="white")
        third_label.place(height=30, width=215, x=20, y=120)
        fourth_label = tk.Label(right_panel1, text="4. If true click approve else click decline", font=("Helvetica", 10),background="white")
        fourth_label.place(height=30, width=235, x=20, y=170)

        
        accept_button = tk.Button(more_info_frame, text="Approve", command=lambda: self.destroy_and_accept(more_info_frame, clinic_id), background="green", fg="white",font=(20))
        accept_button.place(height=50, width=350, x=610, y=380)
        decline_button = tk.Button(more_info_frame, text="Decline", background="red", fg="white",font=(20),command=lambda: self.destroy_and_decline(more_info_frame, clinic_id))
        decline_button.place(height=50, width=350, x=610, y=450)
        
        # Display information in the new frame
        clinic_name = tk.Label(more_info_frame, text=selected_record[1], font=("Helvetica", 25),background="#F9F3CC")
        clinic_name.place(height=40, width=300, x=350, y=30)
        

        clinic_info = tk.Label(left_panel1, text="Clinic Information", font=("Helvetica", 20),background="white")
        clinic_info.pack(pady=20)
        clinic_operationTime = tk.Label(left_panel1, text="Operation Time: " + selected_record[2], font=("Helvetica", 10),background="white")
        clinic_operationTime.pack(pady=1,anchor="w")
        clinic_phoneNumber = tk.Label(left_panel1, text="Phone Number: " + selected_record[5], font=("Helvetica", 10),background="white")
        clinic_phoneNumber.pack(pady=1,anchor="w")
        clinic_location = tk.Label(left_panel1, text="Location: " + selected_record[4], font=("Helvetica", 10),background="white",wraplength=400)
        clinic_location.pack(pady=1,anchor="w")
        clinic_codinates = tk.Label(left_panel1, text="Coordinate: " + selected_record[3], font=("Helvetica", 10),background="white")
        clinic_codinates.pack(pady=1,anchor="w")
        clinic_registration = tk.Label(left_panel1, text="Registration Number: " + str(selected_record[6]), font=("Helvetica", 10),background="white")
        clinic_registration.pack(pady=1,anchor="w")
        clinic_description = tk.Label(left_panel1, text="Description: " + selected_record[7], font=("Helvetica", 10),background="white",wraplength=400)
        clinic_description.pack(pady=1,anchor="w")
        founder_info = tk.Label(left_panel1, text="Founder Information", font=("Helvetica", 20),background="white")
        founder_info.pack(pady=20)
        founder_name = tk.Label(left_panel1, text="Founder Name: " + selected_record[8], font=("Helvetica", 10),background="white")
        founder_name.pack(pady=1,anchor="w")
        founder_email = tk.Label(left_panel1, text="Email: " + selected_record[10], font=("Helvetica", 10),background="white")
        founder_email.pack(pady=1,anchor="w")
        founder_phone = tk.Label(left_panel1, text="Contact: " + str(selected_record[9]), font=("Helvetica", 10),background="white")
        founder_phone.pack(pady=1,anchor="w")


    def destroy_and_accept(self, frame, clinic_id):
        # Update the status of the request in the database
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("UPDATE ClinicInformation SET status=1 WHERE clinic_id=?", (clinic_id,))
        self.conn.commit()
        self.conn.close()

        tkinter.messagebox.showinfo("Success", "Clinic Approved Successfully!")

        # Destroy the new frame
        frame.destroy()
        

    def destroy_and_decline(self, frame, clinic_id):

        decline_frame = tk.Frame(self.request_frame, background="white")
        decline_frame.place(height=640, width=1000, x=0, y=60)
        
        decline_label = tk.Label(decline_frame, text="Reason for Decline", font=("Helvetica", 25),background="white")
        decline_label.place(height=30, width=300, x=350, y=30)
        decline_entry = tk.Text(decline_frame,highlightbackground="black", highlightthickness=1, font=("Helvetica", 15))
        decline_entry.place(height=200,width=500, x=250, y=100)

        submit_button = tk.Button(decline_frame, text="Submit", command=lambda: self.destroy_and_submit(decline_frame, clinic_id, decline_entry.get("1.0", "end-1c")), background="green", fg="white",font=(20))
        submit_button.place(height=50, width=350, x=610, y=380)

        # Destroy the new frame
        frame.destroy()
    
    def destroy_and_submit(self, frame, clinic_id, reason):
        # Update the status of the request in the database
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

        # Check if the 'reason' column exists in the table
        self.c.execute("PRAGMA table_info(ClinicInformation)")
        columns = [column[1] for column in self.c.fetchall()]
        if 'reason' not in columns:
            self.c.execute("ALTER TABLE ClinicInformation ADD COLUMN reason VARCHAR(1000)")

        self.c.execute("UPDATE ClinicInformation SET status=2, reason=? WHERE clinic_id=?", (reason, clinic_id,))

        self.conn.commit()
        self.conn.close()

        tkinter.messagebox.showinfo("Success", "Clinic Declined Successfully!")
        
        # Destroy the new frame
        frame.destroy()


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

        refresh_button = Button(self.top_frame1, text="Refresh", command=self.refresh_clinic,background="#F9F3CC")
        refresh_button.place(height=30, width=100, x=100, y=10)

        self.load_clinic(frame_inner)



    def load_clinic(self, frame_inner):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)  # Connect to the existing database
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ClinicInformation WHERE status=1 or status=2")
        displayrecord = self.c.fetchall()

        i = 0
        for _ in displayrecord:
            clinic_frame = Frame(frame_inner, background="white", highlightbackground="black", highlightthickness=1, width=900,height=100)
            clinic_frame.grid(row=i, column=1, padx=1, pady=1)
            clinic_name = Label(clinic_frame, text=displayrecord[i][1], font=("Helvetica", 16), background="white")
            clinic_name.place(x=10, y=20)
            clinic_location = Label(clinic_frame, text="Location : " + displayrecord[i][4], font=("Helvetica", 10), background="white")
            clinic_location.place(x=10, y=50)
            clinic_status = Label(clinic_frame, text="Status : ", font=("Helvetica", 12), background="white")
            clinic_status.place(x=610, y=20)
            if displayrecord[i][13] == 1:
                status = Label(clinic_frame, text="Approved", font=("Helvetica", 12), fg="green", background="white")
                status.place(x=700, y=20)
            elif displayrecord[i][13] == 2:
                status = Label(clinic_frame, text="Declined", font=("Helvetica", 12), fg="red", background="white")
                status.place(x=700, y=20)
            clinic_button = Button(clinic_frame, text="More Information", command=lambda i=i: self.more_information(clinic_id=displayrecord[i][0]),background="#F9F3CC")
            clinic_button.place(height=30, width=150, x=700, y=55)
            i += 1

        self.conn.close()

    def refresh_clinic(self):
        for widget in self.viewClinic_canvas.winfo_children():
            widget.destroy()

        # Fetch and display the latest data
        frame_inner = Frame(self.viewClinic_canvas)
        self.viewClinic_canvas.create_window((0, 0), window=frame_inner, anchor="nw")
        self.load_clinic(frame_inner)

        # Reset the scrollregion of the Canvas
        self.viewClinic_canvas.update_idletasks()  # Ensure all widgets are updated
        self.viewClinic_canvas.config(scrollregion=self.viewClinic_canvas.bbox("all"))

        

    def more_information(self, clinic_id):

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
        clinic_coordinates = tk.Label(left_panel1, text="Coordinates: " + selected_record[3], font=("Helvetica", 10), background="white")
        clinic_coordinates.pack(pady=1, anchor="w")
        clinic_registration = tk.Label(left_panel1, text="Registration Number: " + str(selected_record[6]), font=("Helvetica", 10), background="white")
        clinic_registration.pack(pady=1, anchor="w")
        clinic_description = tk.Label(left_panel1, text="Description: " + selected_record[7], font=("Helvetica", 10), background="white")
        clinic_description.pack(pady=1, anchor="w")
        clinic_description.pack(pady=1,anchor="w")
        founder_info = tk.Label(left_panel1, text="Founder Information", font=("Helvetica", 20),background="white")
        founder_info.pack(pady=20)
        founder_name = tk.Label(left_panel1, text="Founder Name: " + selected_record[8], font=("Helvetica", 10),background="white")
        founder_name.pack(pady=1,anchor="w")
        founder_email = tk.Label(left_panel1, text="Email: " + selected_record[10], font=("Helvetica", 10),background="white")
        founder_email.pack(pady=1,anchor="w")
        founder_phone = tk.Label(left_panel1, text="Contact: " + str(selected_record[9]), font=("Helvetica", 10),background="white")
        founder_phone.pack(pady=1,anchor="w")

        status_label = tk.Label(more_info_frame, text="Status: ", font=("Helvetica", 15),background="#F9F3CC")
        status_label.place(height=30, width=100, x=610, y=100)
        if selected_record[13] == 1:
            status = tk.Label(more_info_frame, text="Approved", font=("Helvetica", 15),background="#F9F3CC", fg="green")
            status.place(height=30, width=200, x=700, y=100)
        elif selected_record[13] == 2:
            status = tk.Label(more_info_frame, text="Declined", font=("Helvetica", 15),background="#F9F3CC", fg="red")
            status.place(height=30, width=200, x=700, y=100)
            reason_label = tk.Label(more_info_frame, text="Reason: ", font=("Helvetica", 15),background="#F9F3CC")
            reason_label.place(height=30, width=100, x=610, y=150)
            reason = tk.Label(more_info_frame, text=selected_record[14], font=("Helvetica", 15),background="white",highlightthickness=1, highlightbackground="black",wraplength=300)
            reason.place(height=100, width=300, x=610, y=200)


class ViewTipsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.tipsView_frame = Frame(self, background="white")
        self.tipsView_frame.place(height=700, width=1000)

        #### Top Panel #######

        self.top_frame1 = Frame(self.tipsView_frame , background="#D2E0FB")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        TipsView_label  = Label(self.top_frame1 ,  text="Health Tips For You", font=("Helvetica", 24),background = "#D2E0FB")
        TipsView_label .pack()

        back_btn = Button(self, text="Back", background="#F9F3CC", command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100, x=700, y=10)

        refresh_btn = Button(self, text="Refresh", background="#F9F3CC", command=self.refresh_tips)
        refresh_btn.place(height=30, width=100, x=800, y=10)

        self.frame2 = Frame(self.tipsView_frame, background="#D2E0FB")
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.tips_canvas = Canvas(self.frame2, background="#F9F3CC")
        self.tips_canvas.place(height=550, width=900, x=0, y=0)

        scrollbar = Scrollbar(self.frame2, orient=VERTICAL, command=self.tips_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tips_canvas.configure(yscrollcommand=scrollbar.set)
        self.tips_canvas.bind('<Configure>', lambda _: self.tips_canvas.configure(scrollregion=self.tips_canvas.bbox("all")))

        frame_inner = Frame(self.tips_canvas)
        self.tips_canvas.create_window((0, 0), window=frame_inner, anchor="nw")

        self.load_tips(frame_inner)

    def load_tips(self, frame_inner):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM TIPS")
        displayrecord = self.c.fetchall()

        i = 0
        for TIPS in displayrecord:
            tips_frame = Frame(frame_inner, background="white", highlightbackground="black", highlightthickness=1, width=880, height=180)
            tips_frame.grid(row=i, column=1, padx=1, pady=1)

            tips_label = Label(tips_frame, border=0, text=TIPS[1], font=("Helvetica", 16), background="white")
            tips_label.place(x=10, y=10)

            tips_description = Label(tips_frame, border=0, text=TIPS[2], font=("Helvetica", 12), background="white")
            tips_description.place(x=10, y=40)

            tips_link = Label(tips_frame, border=0, text= TIPS[3], font=("Helvetica", 10), fg="blue", cursor="hand2", background="white")
            tips_link.place(x=10, y=130)
            tips_link.bind("<Button-1>", lambda e, url=TIPS[3]: self.open_link(url))

            i += 1

        self.conn.close()

    def open_link(self, url):
        webbrowser.open_new(url)

    def refresh_tips(self):
        # Clear the existing data in the canvas
        for widget in self.tips_canvas.winfo_children():
            widget.destroy()

        # Fetch and display the latest data
        frame_inner = Frame(self.tips_canvas)
        self.tips_canvas.create_window((0, 0), window=frame_inner, anchor="nw")
        self.load_tips(frame_inner)

        # Reset the scrollregion of the Canvas
        self.tips_canvas.update_idletasks()  # Ensure all widgets are updated
        self.tips_canvas.config(scrollregion=self.tips_canvas.bbox("all"))



if __name__ == "__main__":
        app = Application()
        app.geometry('1000x700')
        app.resizable(True, True)
        app.title('Call A Doctor')

        app.mainloop()


