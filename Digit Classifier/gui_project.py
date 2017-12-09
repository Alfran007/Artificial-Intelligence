# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Author: Syed Alfran Ali
from tkinter import *
from PIL import ImageTk, Image
import os
 
def erbt():
    exec(open("./graph.py").read(), globals())
    
def testdbth():
    os.system("python ./prog1.py")
    
def testdb():
    exec(open("./prog1.py").read(), globals())
    
class Application(Frame):
        def __init__(self,master=None):
            Frame.__init__(self,master)
            
            self.grid()
            w = Label(self, text="HANDWRITTEN DIGIT RECOGNITION", font=("Monotype Corsiva", 30,"bold"),fg="brown")
            w.pack()
            im1=Image.open("img0.png")
            render = ImageTk.PhotoImage(im1)
            img = Label(self, image=render)
            img.image = render
            img.pack()
            b1 = Button(self, text="Show Error Rate" ,font=("Times", 12,"bold"),fg="blue",command=erbt)
            b2 = Button(self, text="Test Database",font=("Times", 12,"bold"),fg="blue", command=testdbth)
            b3 = Button(self, text="Find Contours",font=("Times", 12,"bold"),fg="blue")
            b1.pack(fill="both",expand=True,padx=270,pady=10)
            b2.pack(fill="both",expand=True,padx=270,pady=10)
            b3.pack(fill="both",expand=True,padx=270,pady=10)
           
        
app=Application()

app.master.title("Digit Recognition")
app.master.geometry("700x700+200+80")
app.mainloop()            
