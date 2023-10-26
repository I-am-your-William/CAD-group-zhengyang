from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import webbrowser
from PIL import Image, ImageTk
import tkintermapview as tkmap
root=Tk()
root.geometry("1000x900")
root.title("Search Bar")
root.config(bg="#2FBFF2")

lbl1=Label(root,text="Search Here",font=("Roboto",16),bg="#2FBFF2")
lbl1.place(x=10,y=20)
sbox=Entry(root,width=45,font=("Roboto",16))
sbox.place(x=150,y=20)
sbox.focus()
keyin=StringVar()
rbutton1=ttk.Radiobutton(root,text='Google',value='google',variable=keyin)
rbutton1.place(x=150,y=50)
rbutton2=ttk.Radiobutton(root,text='Edge',value='edge',variable=keyin)
rbutton2.place(x=375,y=50)
rbutton3=ttk.Radiobutton(root,text='CAD Map',value='map',variable=keyin)
rbutton3.place(x=600,y=50)
keyin.set('google')
#Search Function
def search():
        fetch_query = sbox.get().lower()
        
        if sbox.get()!='':
            if keyin.get()=='google':
                webbrowser.open(f'https://www.google.com/search?q={sbox.get()}')
            elif keyin.get()=='edge':
                webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open(f'https://www.google.com/search?q={sbox.get()}')
            elif keyin.get()=='map':
                 map_widget.set_address(sbox.get(), marker=True)
                 map_slider.config(value=15)
        else:
            messagebox.showerror("No Input","Oi Type Something la CB")
                 
img=Image.open("C:\DOC\Documents\ZzJS\pStuff\search.png")
phimg=ImageTk.PhotoImage(img)
sbtn=Button(root,image=phimg,width=30,height=30,bg="#2FBFF2",bd=0,command=search)
sbtn.place(x=710,y=18)

map_widget=tkmap.TkinterMapView(root, width=800, height=600, corner_radius=0)
map_widget.place(x=20,y=150)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

#Slide Function
def slide(e):
    map_widget.set_zoom(map_slider.get())

#Map Slider(Zoom)
lbl2=Label(root,text="Zoom Level",font=("Roboto",16),bg="#2FBFF2")
lbl2.place(x=12,y=100)
map_slider=ttk.Scale(root,from_=5,to=25, orient=HORIZONTAL, command=slide, length=200)
map_slider.set(18)
map_slider.place(x=150,y=100)

#Set position either by coordinates(set_position) or address(set_address)
marker1=map_widget.set_position(5.3416,100.2819, marker=True)



root.mainloop()