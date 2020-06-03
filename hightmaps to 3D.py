import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import cv2
from tkinter import *

def execute():
    plt.close()
    img = cv2.imread(path_E.get(),0)
    print img
    plt.imshow(img)
    Z = cv2.flip(cv2.resize(img, (int(res_E.get()),int(res_E.get()))), 1)
    X = np.arange(0,Z.shape[0])
    Y = X
    X,Y = np.meshgrid(X,Y)
    print Z.shape

    fig = plt.figure()
    fig = fig.gca(projection='3d')
    fig.plot_surface(X, Y, Z, cmap=cm.coolwarm)
    plt.show()

menu = Tk()
menu.title("Hightmap to 3D-Plot")
path_L = Label(menu, text = "Dateipfad:")
path_E = Entry(menu)
path_L.pack()
path_E.pack()

res_L = Label(menu, text = "Aufloesung")
res_E = Entry(menu)
res_L.pack()
res_E.pack()

apply_B = Button(menu, text = "apply", command = execute)
apply_B.pack()

menu.mainloop()