import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import Image, ImageTk

root = tk.Tk() 
root.geometry('1300x700')
root.resizable(True, True)
root.title('Call A Doctor')

frame1=tk.Frame(root)
frame2=tk.Frame(root)
frame3=tk.Frame(root)

for frame in (frame1, frame2, frame3):
    frame.place(x=0,y=0,relheight=1,relwidth=1)
    frame.config(bg="#FFFFFF")

############log out#######
def log_out(): 
    root.destroy()

##########################

############Show Frame#############
def show_frame(frame):
    frame.tkraise()
###################################

###########Top Panel #############
top_frame = Frame( frame1, background="light grey")
top_frame.place(height=60, width=1300, x=1, y=1)

heading_label = Label(top_frame, text="Doctor", font=("Helvetica", 24),background = "light grey")
heading_label.pack()

log_out_btn = Button(top_frame , text = " Log Out",background="white",command = log_out)
log_out_btn.place(height=30, width=100,x=800, y=10)

# Create a canvas that can fit the above image
image = Image.open('C:/Users/MyAcer/Desktop/Software engineering/Image folder/Icon CDA.png')
label_width, label_height = 40, 40
image = image.resize((label_width, label_height), Image.LANCZOS)  # Use Image.LANCZOS for resizing

# Create a PhotoImage from the resized image
image = ImageTk.PhotoImage(image)

label = Label(top_frame, image=image)
label.image = image  # Keep a reference to the image to prevent garbage collection
label.place(height=label_height, width=label_width, x=15, y=15)

#######left side panel########
left_side_panel = Frame(frame1, background="light grey")
left_side_panel.place(height=550, width=300, x=55, y=100)

patient_btn = Button ( frame1, text = "Patient", font=(20),background="white",command=lambda:show_frame(frame2))
patient_btn.place(height=70,width=200, x=100, y=160)

History_btn = Button ( frame1, text = " History ", font=(20),background="white")
History_btn.place(height=70,width=200, x=100, y=270)



#right side panel
right_side_panel = Frame(frame1, background="light grey")
right_side_panel.place(height=550, width=870, x=390, y=100)

lfs_right_panel =Frame(frame1 , bg="white")
lfs_right_panel.place(height=500 , width=400 , x=410 , y=120)

accept1=Button(frame1 , text="Accept",bg="#CBC3E3",fg="white",font="Roboto 10")
accept1.place(width=150,height=30,x=420,y=570)

reject1=Button(frame1 , text="Reject",bg="#CBC3E3",fg="white",font="Roboto 10")
reject1.place(width=150,height=30,x=640,y=570)

rhs_right_panel =Frame(frame1 , bg="white")
rhs_right_panel.place(height=500 , width=400 , x=840 , y=120)

JoinMeeting=Button(frame1, text="Join Meeting Now",bg="#CBC3E3",fg="white",font="Roboto 10")
JoinMeeting.place(width=380,height=30,x=850,y=570)

Appointment_upcoming=Label(lfs_right_panel, text="Appointment Upcoming", font=("Helvetica", 10),background="#FFFFFF")
Appointment_upcoming.pack()

Appointment_Pending=Label(rhs_right_panel, text="Appointment Pending", font=("Helvetica", 10),background="#FFFFFF")
Appointment_Pending.pack()


####################Frame 2 design######################
top_frame2 = Frame( frame2, background="light grey")
top_frame2.place(height=60, width=1300, x=1, y=1)
label2 = Label(top_frame2, image=image)
label2.image = image  # Keep a reference to the image to prevent garbage collection
label2.place(height=label_height, width=label_width, x=15, y=15)

heading_label = Label(top_frame2, text="Patient Information", font=("Helvetica", 24),background = "light grey")
heading_label.pack()

log_out_btn = Button(top_frame2 , text = " Log Out",background="white",command = log_out)
log_out_btn.place(height=30, width=100,x=800, y=10)

right_side_panel2 = Frame(frame2, background="light grey")
right_side_panel2.place(height=550, width=870, x=390, y=100)

lfs_right_panel2 =Frame(frame2 , bg="white")
lfs_right_panel2.place(height=500 , width=400 , x=410 , y=120)

rhs_right_panel2 =Frame(frame2 , bg="white")
rhs_right_panel2.place(height=500 , width=400 , x=840 , y=120)

left_side_panel2 = Frame(frame2, background="light grey")
left_side_panel2.place(height=550, width=300, x=55, y=100)

back_btn = Button ( frame2, text = "Back to Doctor", font=(20),background="white",command=lambda:show_frame(frame1))
back_btn.place(height=70,width=200, x=100, y=300)

History_label=Label(lfs_right_panel2, text="History", font=("Helvetica", 24),background="#FFFFFF")
History_label.pack()

textSignUp=tk.Label(frame2,text="Patient:", font='Roboto 16',fg="#7F00FF",bg="#FFFFFF")
textSignUp.pack()
textSignUp.place(x=100,y=150)
comboSignup=ttk.Combobox(frame2,values=["Patient1","Patient2","Patient3","Patient4","Patient5"],width=30)
comboSignup.pack()
comboSignup.place(x=100,y=200)
Prescription_label=Label(rhs_right_panel2, text="Prescription", font=("Helvetica", 24),background="#FFFFFF")
Prescription_label.pack()
########################################################
# Run the Tkinter main loop
show_frame(frame1)
root.mainloop()