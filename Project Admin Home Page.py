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
        self.title_label.place(x=50, y=100)
        self.title_entry = Entry(self.frame2)
        self.title_entry.place(height=30,width=200, x=150, y=100)

        self.content_label = Label(self.frame2, text = "Content Description : ", font=(20),background = "light grey")
        self.content_label.place(x=50, y=150)
        self.content_entry = Entry(self.frame2)
        self.content_entry.place(height=30,width=200, x=50, y=190)

        self.link_label = Label(self.frame2, text = "Link : ", font=(20),background = "light grey")
        self.link_label.place(x=50, y=250)
        self.link_entry = Entry(self.frame2)
        self.link_entry.place(height=30,width=200, x=150, y=250)

        upload_btn = Button(self.frame2, text = "Upload",background="white", font=(20))
        upload_btn.place(height=50, width=100,x=50, y=300)




class ManagePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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
        self.content_entry = Entry(self.frame2)
        self.content_entry.place(height=30,width=200, x=50, y=140)

        self.link_label = Label(self.frame2, text = "Link : ", font=(20),background = "light grey")
        self.link_label.place(x=50, y=200)
        self.link_entry = Entry(self.frame2)
        self.link_entry.place(height=30,width=200, x=150, y=200)

        save_btn = Button(self.frame2, text = "Save",background="white", font=(20))
        save_btn.place(height=40, width=100,x=50, y=250)

        delete_btn = Button(self.frame2, text = "Delete",background="white", font=(20))
        delete_btn.place(height=40, width=100,x=150, y=250)


        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", bg="#D3D3D3", fg="black", rowheight=20, fieldbackground="#F8F8F8")
        style.map("Treeview", bg=[('selected', "#F9ECE4")])


        thetreeframe = Frame(self.frame2)
        thetreeframe.place(x=10,y=300)

        treescroll = Scrollbar(thetreeframe)
        treescroll.pack(side=RIGHT, fill=Y)

        manage_tree = ttk.Treeview(thetreeframe, yscrollcommand=treescroll.set, selectmode="extended")
        manage_tree.pack()

        treescroll.config(command=manage_tree.yview)

        manage_tree['column'] = ('1', '2', '3', '4')
        manage_tree['show'] = 'headings'

        manage_tree.column('1', width=50, anchor='c')
        manage_tree.column('2', width=250, anchor='c')
        manage_tree.column('3', width=300, anchor='c')
        manage_tree.column('4', width=250, anchor='c')

        manage_tree.heading('1', text='ID')
        manage_tree.heading('2', text='Title')
        manage_tree.heading('3', text='Content')
        manage_tree.heading('4', text='Link')
    
        manage_tree.tag_configure('odd', background="lightblue")
        manage_tree.tag_configure('even', background="white")

       
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
