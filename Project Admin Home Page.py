import tkinter as tk
from tkinter import *
from tkinter import ttk
import  tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3


LARGEFONT = ("Verdana", 35)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, UploadPage, ManagePage, ClinicRequestPage, ViewAllClinicPage ) :
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
        self.controller = controller

        ###########Top Panel #############

        home_page = Frame(self ,background="white")
        home_page.place(height=700, width=1000,x=0,y=0)

        self.top_frame = Frame(home_page , background="light grey")
        self.top_frame.place(height=60, width=1000, x=1, y=1)

        heading_label = Label(self.top_frame ,  text="Call A Doctor Admin Home Page", font=("Helvetica", 24),background = "light grey")
        heading_label.pack()

        log_out_btn = Button(self.top_frame, text = " Log Out",background="white",command = self.log_out)
        log_out_btn.place(height=30, width=100,x=800, y=10)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 40, 40
        image = image.resize((label_width, label_height), Image.LANCZOS)  # Use Image.LANCZOS for resizing

        # Create a PhotoImage from the resized image
        image = ImageTk.PhotoImage(image)

        label = Label(self.top_frame, image=image)
        label.image = image  # Keep a reference to the image to prevent garbage collection
        label.place(height=label_height, width=label_width, x=15, y=15)

        #######left side panel########
        self.left_side_panel = Frame(home_page , background="light grey")
        self.left_side_panel.place(height=550, width=300, x=55, y=100)

        view_clinic_btn = Button (self.left_side_panel , text = " View All Clinic ", font=(20),background="white",command=lambda: controller.show_frame(ViewAllClinicPage))
        view_clinic_btn.place(height=70,width=200, x=50, y=50)

        upload_tip_btn = Button (self.left_side_panel, text = " Upload Tips ", font=(20),background="white", command=lambda: controller.show_frame(UploadPage))
        upload_tip_btn.place(height=70,width=200, x=50, y=200)

        manage_tip_btn = Button (self.left_side_panel , text = " Manage Tips ", font=(20),background="white", command=lambda: controller.show_frame(ManagePage))
        manage_tip_btn.place(height=70,width=200, x=50, y=350)

        #right side panel
        self.right_side_panel = Frame(home_page , background="light grey")
        self.right_side_panel.place(height=550, width=550, x=390, y=100)

        request_btn = Button (self.right_side_panel, text = " Clinic Request  ", font=(20), background="white", command=lambda: controller.show_frame(ClinicRequestPage) )
        request_btn.place(height=70, width=450, x=50, y=50)

        right_frame = Frame(self.right_side_panel, background="white")
        right_frame.place(height=350, width=450, x=50, y=150)

    def log_out(self):
         self.controller.destroy()

class UploadPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        self.upload_frame = Frame(self, background="white")
        self.upload_frame.place(height=700, width=1000)
        

        #### Top Panel #######

        self.top_frame1 = Frame(self.upload_frame , background="light grey")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        upload_label  = Label(self.top_frame1 ,  text="Upload Tips Page", font=("Helvetica", 24),background = "light grey")
        upload_label .pack()

        back_btn = Button(self, text = "Back",background="white",command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100,x=800, y=10)

        #### Main Frame ######

        self.frame2 = Frame(self.upload_frame , background = "light grey" )
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.title_label = Label(self.frame2, text = "Tilte : ", font=(20),background = "light grey")
        self.title_label.place(x=50, y=30)
        self.title_entry = Entry(self.frame2)
        self.title_entry.place(height=30,width=200, x=150, y=30)

        self.content_label = Label(self.frame2, text = "Content Description : ", font=(20),background = "light grey")
        self.content_label.place(x=50, y=80)
        self.content_entry = Text(self.frame2)
        self.content_entry.place(height=90,width=310, x=50, y=120)

        self.link_label = Label(self.frame2, text = "Link : ", font=(20),background = "light grey")
        self.link_label.place(x=50, y=250)
        self.link_entry = Entry(self.frame2)
        self.link_entry.place(height=30,width=200, x=150, y=250)

        upload_btn = Button(self.frame2, text = "Upload",background="white", font=(20),command=self.upload)
        upload_btn.place(height=50, width=100,x=50, y=300)

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
            self.conn = sqlite3.connect("CAD_Database.db")  # Connect to the database
            self.c = self.conn.cursor()  # Create a cursor
            self.c.execute(
                """CREATE TABLE IF NOT EXISTS TIPS(
                    Post_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    TITLE VARCHAR (100) NOT NULL, 
                    CONTENT VARCHAR (1000)  NOT NULL,
                    LINK VARCHAR (100) NOT NULL)"""
            )
            self.c.execute(
                "INSERT INTO TIPS ( TITLE, CONTENT, LINK) VALUES(?,?,?)",
                ( self.title_entry_submit, self.content_entry_submit, self.link_entry_submit),
            )
            new_post_id = self.c.lastrowid 
            self.conn.commit()  # This line physically enters the data into the database.
            self.conn.close()
            tkinter.messagebox.showinfo("Data saved")
            self.clearTextInput()

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

        self.top_frame1 = Frame(self.manage_frame , background="light grey")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        manage_label  = Label(self.top_frame1 ,  text="Manage Tips Page", font=("Helvetica", 24),background = "light grey")
        manage_label .pack()

        back_btn = Button(self, text = "Back",background="white",command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100,x=800, y=10)

        ####### Main frame ) 

        self.frame2 = Frame(self.manage_frame , background = "light grey" )
        self.frame2.place(height=550, width=900, x=55, y=100)

        self.title_label = Label(self.frame2, text = "Tilte : ", font=(20),background = "light grey")
        self.title_label.place(x=50, y=50)
        self.title_entry = Entry(self.frame2)
        self.title_entry.place(height=30,width=200, x=150, y=50)

        self.content_label = Label(self.frame2, text = "Content Description : ", font=(20),background = "light grey")
        self.content_label.place(x=50, y=100)
        self.content_entry = Text(self.frame2)
        self.content_entry.place(height=90,width=310, x=250, y=100)

        self.link_label = Label(self.frame2, text = "Link : ", font=(20),background = "light grey")
        self.link_label.place(x=50, y=200)
        self.link_entry = Entry(self.frame2)
        self.link_entry.place(height=30,width=200, x=150, y=200)

        save_btn = Button(self.frame2, text = "Save",background="white", font=(20),command=self.save)
        save_btn.place(height=40, width=100,x=50, y=250)

        delete_btn = Button(self.frame2, text = "Delete",background="white", font=(20),command=self.delete)
        delete_btn.place(height=40, width=100,x=150, y=250)


        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", bg="#D3D3D3", fg="black", rowheight=20, fieldbackground="#F8F8F8")
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
    
        tree_tips.tag_configure('odd', background="light grey")
        tree_tips.tag_configure('even', background="white") 
        
        

        
        self.conn = sqlite3.connect("CAD_Database.db")
        self.c = self.conn.cursor()
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
        self.conn = sqlite3.connect("CAD_Database.db")
        self.c = self.conn.cursor()
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
            self.conn = sqlite3.connect("CAD_Database.db")
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


    def select_item(self, a):
        tree_item = tree_tips.focus()
        values = tree_tips.item(tree_item, 'values')
        self.title_entry.delete(0, END)
        self.title_entry.insert(0, values[1])
        self.content_entry.delete('1.0', END)
        self.content_entry.insert('1.0', values[2])
        self.link_entry.delete(0, END)
        self.link_entry.insert(0, values[3])

    def delete(self):
        selected_item = tree_tips.selection()
        if not selected_item:
            tkinter.messagebox.showinfo("Error", "Please select a record to delete.")
            return

        selected_item = selected_item[0]
        try:
            self.conn = sqlite3.connect("CAD_Database.db")
            self.c = self.conn.cursor()
            post_id = tree_tips.item(selected_item, 'values')[0]
            
            # Check if the record still exists in the database before deleting
            self.c.execute("SELECT * FROM TIPS WHERE Post_ID=?", (post_id,))
            record = self.c.fetchone()
            
            if record:
                self.c.execute("DELETE FROM TIPS WHERE Post_ID=?", (post_id,))
                self.conn.commit()
                self.conn.close()
                tree_tips.delete(selected_item)
                self.clearTextInput()
                tkinter.messagebox.showinfo("Success", "Record Deleted Successfully!")
            else:
                tkinter.messagebox.showinfo("Error", "Record not found in the database.")
        except Exception as e:
            print(f"Error while deleting record: {str(e)}")

       
class ClinicRequestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.request_frame = Frame(self, background="white")
        self.request_frame.place(height=700, width=1000)

        #### Top Panel #######

        self.top_frame2 = Frame(self.request_frame , background="light grey")
        self.top_frame2.place(height=60, width=1000, x=1, y=1)

        request_label  = Label(self.top_frame2 ,  text="Clinic Request Page", font=("Helvetica", 24),background = "light grey")
        request_label .pack()

        back_btn = Button(self, text = "Back",background="white",command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100,x=800, y=10)
        
        ############# 

class ViewAllClinicPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.clinicView_frame = Frame(self, background="white")
        self.clinicView_frame.place(height=700, width=1000)

        #### Top Panel #######

        self.top_frame1 = Frame(self.clinicView_frame , background="light grey")
        self.top_frame1.place(height=60, width=1000, x=1, y=1)

        clinicView_label  = Label(self.top_frame1 ,  text="View Clinic Page", font=("Helvetica", 24),background = "light grey")
        clinicView_label .pack()

        back_btn = Button(self, text = "Back",background="white",command=lambda: controller.show_frame(HomePage))
        back_btn.place(height=30, width=100,x=800, y=10)


if __name__ == "__main__":
    app = Application()
    app.geometry('1000x700')
    app.resizable(True, True)
    app.title('Call A Doctor')
    app.mainloop()


