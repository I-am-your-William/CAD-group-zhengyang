from tkinter import *
from PIL import ImageTk, Image

root = Tk() 
root.geometry('1300x700')
root.resizable(True, True)
root.title('Call A Doctor')

############log out#######
def log_out(): 
    root.destroy()

###########Top Panel #############
top_frame = Frame(master = root, background="light grey")
top_frame.place(height=60, width=1300, x=1, y=1)

heading_label = Label(master = top_frame, text="Doctor", font=("Helvetica", 24),background = "light grey")
heading_label.pack()

log_out_btn = Button(master = top_frame , text = " Log Out",background="white",command = log_out)
log_out_btn.place(height=30, width=100,x=800, y=10)


image = Image.open('C:/Users/MyAcer/Desktop/Software engineering/Image folder/Icon CDA.png')
label_width, label_height = 40, 40
image = image.resize((label_width, label_height), Image.LANCZOS)  # Use Image.LANCZOS for resizing

# Create a PhotoImage from the resized image
image = ImageTk.PhotoImage(image)

label = Label(top_frame, image=image)
label.image = image  # Keep a reference to the image to prevent garbage collection
label.place(height=label_height, width=label_width, x=15, y=15)

#######left side panel########
left_side_panel = Frame(master = root, background="light grey")
left_side_panel.place(height=550, width=300, x=55, y=100)

patient_btn = Button (master = root, text = "Patient", font=(20),background="white")
patient_btn.place(height=70,width=200, x=100, y=160)

History_btn = Button (master = root, text = " History ", font=(20),background="white")
History_btn.place(height=70,width=200, x=100, y=270)



#right side panel
right_side_panel = Frame(master = root, background="light grey")
right_side_panel.place(height=550, width=870, x=390, y=100)

lfs_right_panel =Frame(master=root , bg="white")
lfs_right_panel.place(height=500 , width=400 , x=410 , y=120)

accept1=Button(master=root , text="Accept",bg="#CBC3E3",fg="white",font="Roboto 10")
accept1.place(width=150,height=30,x=420,y=570)

reject1=Button(master=root , text="Reject",bg="#CBC3E3",fg="white",font="Roboto 10")
reject1.place(width=150,height=30,x=640,y=570)

rhs_right_panel =Frame(master=root , bg="white")
rhs_right_panel.place(height=500 , width=400 , x=840 , y=120)

accept2=Button(master=root , text="Accept",bg="#CBC3E3",fg="white",font="Roboto 10")
accept2.place(width=150,height=30,x=850,y=570)

reject2=Button(master=root , text="Reject",bg="#CBC3E3",fg="white",font="Roboto 10")
reject2.place(width=150,height=30,x=640,y=570)

# Run the Tkinter main loop
root.mainloop()