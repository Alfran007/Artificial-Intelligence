#Author: Syed Alfran Ali
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from PIL import Image
digits=datasets.load_digits()
tr=[1,10,100,500,750,1000,1500,1797]
er=[]
min_index = 0
for k in range(0,len(tr)):
    #testing i image
    x_train=digits.data[0:tr[k]]
    y_train=digits.target[0:tr[k]]

    def dist(a,b):
        return np.sqrt(np.sum((a-b)**2))

    n=len(x_train)
    #testing 100 images
    e=0
    dista=np.zeros(n)
    for j in range(1697,1797):
        x_test=digits.data[j]
        for i in range(0,n):
            dista[i]=dist(x_train[i],x_test)
        min_index=np.argmin(dista)
        if y_train[min_index]!=digits.target[j]:
            e+=1
    er.append(e)
print(er)
fig1=plt.figure()
plt.plot(tr, er, '#54fff7', linewidth=3)
plt.grid(True)
plt.title("Error rate v/s No. of Training Images")
plt.xlabel("No. of Training Images")
plt.ylabel("Error Rate")
plt.show()
fig1.savefig("error.png")
im1=Image.open("error.png")
im1.show()
