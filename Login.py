import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import Image, ImageTk


root=tk.Tk()
root.geometry("1440x500")
root.title("Login")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1=tk.Frame(root)
frame2=tk.Frame(root)
frame3=tk.Frame(root)


for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')
    frame.config(bg="#FFFFFF")

####Image Insertion#####
logo_image = Image.open('C:\Users\Wong Joe Shen\Documents(C)\Snips(C)\CDA-Icon.png')  # Replace with the path to your logo image
logo_photo = ImageTk.PhotoImage(logo_image)
########################

def show_frame(frame):
    frame.tkraise()

#F1
logo = Label(frame1, image=logo_photo,bg="#FFFFFF")#Logo Photo
logo.pack()
logo.place(x=620,y=50)
title = tk.Label(frame1, text='Username/Email', font='Roboto 16',bg="#FFFFFF")#Word
title.pack()
title.place(x=554,y=220)
E1=tk.Entry(frame1,width=50)#Entry
E1.pack()
E1.place(x=554, y=250)
title2 = tk.Label(frame1, text='Password', font='Roboto 16',bg="#FFFFFF")
title2.pack()
title2.place(x=554,y=270)
E2=tk.Entry(frame1,width=50)
E2.pack()
E2.place(x=554, y=300)
Forgot = tk.Label(frame1, text='Forgot Password?', font='Roboto 16 underline bold',fg="blue",bg="#FFFFFF")
Forgot.pack()
Forgot.place(x=554,y=320)

Login_Button=tk.Button(frame1, text="Login",bg="Blue",fg="White",width=25,font='Roboto 12')
Login_Button.pack()
Login_Button.place(x=500,y=370)

Register_Button=tk.Button(frame1, text="Register",bg="Blue",fg="White",width=25,font='Roboto 12',command=lambda:show_frame(frame2))
Register_Button.pack()
Register_Button.place(x=745,y=370)
#F1

#F2
logo_image2 = logo_image.resize((170, 130))
logo_photo2 = ImageTk.PhotoImage(logo_image2)
logo2 = Label(frame2, image=logo_photo2)#Logo Photo
logo2.pack()
logo2.place(x=0,y=0)
title2 = tk.Label(frame2, text='Registration', font='Roboto 20 bold underline',bg="#FFFFFF")#Word
title2.pack()
title2.place(x=200,y=50)
textUsername=tk.Label(frame2,text="Username", font='Roboto 16',fg="#7F00FF",bg="#FFFFFF")
textUsername.pack()
textUsername.place(x=10,y=150)
Username_input_registeration=tk.Entry(frame2,width=50,bg="#ADD8E6")
Username_input_registeration.pack()
Username_input_registeration.place(x=10,y=180)
textPassword=tk.Label(frame2,text="Password", font='Roboto 16',fg="#7F00FF",bg="#FFFFFF")
textPassword.pack()
textPassword.place(x=10,y=200)
Password_input_registeration=tk.Entry(frame2,width=50,bg="#ADD8E6")
Password_input_registeration.pack()
Password_input_registeration.place(x=10,y=230)
textEmail=tk.Label(frame2,text="Email", font='Roboto 16',fg="#7F00FF",bg="#FFFFFF")
textEmail.pack()
textEmail.place(x=10,y=250)
Email_input_registeration=tk.Entry(frame2,width=50,bg="#ADD8E6")
Email_input_registeration.pack()
Email_input_registeration.place(x=10,y=280)
textContact=tk.Label(frame2,text="Contact No.", font='Roboto 16',fg="#7F00FF",bg="#FFFFFF")
textContact.pack()
textContact.place(x=450,y=150)
Contact_input_registeration=tk.Entry(frame2,width=50,bg="#ADD8E6")
Contact_input_registeration.pack()
Contact_input_registeration.place(x=450,y=180)
textIC=tk.Label(frame2,text="IC No.", font='Roboto 16',fg="#7F00FF",bg="#FFFFFF")
textIC.pack()
textIC.place(x=450,y=200)
IC_input_registeration=tk.Entry(frame2,width=50,bg="#ADD8E6")
IC_input_registeration.pack()
IC_input_registeration.place(x=450,y=230)
textSignUp=tk.Label(frame2,text="I am signing up as:", font='Roboto 16',fg="#7F00FF",bg="#FFFFFF")
textSignUp.pack()
textSignUp.place(x=900,y=150)
comboSignup=ttk.Combobox(frame2,values=["Doctor","Staff","Project Administrator","Patient"],width=50)
comboSignup.pack()
comboSignup.place(x=900,y=180)
Register2_Button=tk.Button(frame2, text="Register",bg="Blue",fg="White",width=25,font='Roboto 12',command=lambda:show_frame(frame1))
Register2_Button.pack()
Register2_Button.place(x=450,y=280)


show_frame(frame1)
root.mainloop()