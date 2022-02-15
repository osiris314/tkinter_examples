#LINK FOR CHART OPTIONS BELLOW:
#https://matplotlib.org/3.3.3/tutorials/introductory/sample_plots.html
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt



root = Tk()
root.title('12')
root.iconbitmap('images/5_logo.ico')
root.geometry('400x200')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)#average price / diviation / data points
    plt.hist(house_prices, 200)#how many slices
    plt.show()#display plt

my_btn = Button(root, text='GRAPH', command=graph)
my_btn.pack()

root.mainloop()