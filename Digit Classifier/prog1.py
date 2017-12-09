# Author : Syed Alfran Ali
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
from sklearn import datasets
import random

tnum=random.randint(1001,1797)
digits=datasets.load_digits()
x_train=digits.data[0:100]
y_train=digits.target[0:100]
n=len(x_train)
x_test=digits.data[tnum]
y_test=digits.target[tnum]
def dist(a,b):
    return np.sqrt(np.sum((a-b)**2))

def test(label):
    dista=np.zeros(n)
    for i in range(0,n):
        dista[i]=dist(x_train[i],x_test)

    min_index=np.argmin(dista)
    print(y_train[min_index],y_test)
    print(type(digits.images[0]))
    label.configure(text=str(y_train[min_index]), font=("Arial", 15,"bold"),fg="purple")


class Application1(Frame):
        def __init__(self,master=None):
            Frame.__init__(self,master)
            self.grid()
            w = Label(self, text="Testing of Image in Sklearn Database", font=("Monotype Corsiva", 30,"bold"),fg="green")
            w.pack()
            fig1=plt.figure()
            plt.imshow(digits.images[tnum], cmap=plt.cm.gray_r,interpolation='nearest')
            plt.axis("off")
            fig1.savefig("testim.png")
            im1=Image.open("testim.png")
            im1.resize((100,100))
            render = ImageTk.PhotoImage(im1)
            img = Label(self, image=render)
            img.image = render
            img.pack()
            out=Label(self)
            b1 = Button(self, text="Test" ,font=("Times", 12,"bold"),fg="blue",command=lambda label=out:test(label))
            b1.pack(fill="both",expand=True,padx=270,pady=10)
            out.pack()
            '''b1 = Button(self, text="Restart" ,font=("Times", 12,"bold"),fg="blue",command=rerun)
            b1.pack(fill="both",expand=True,padx=270,pady=10)'''
            #test()
app1=Application1()

app1.master.title("Digit Recognition")
app1.master.geometry("600x700+100+80")
app1.mainloop()     
