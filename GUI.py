#Graphical User Interface

from tkinter import *
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from tkinter import messagebox
import _tkinter
window = Tk()
window.geometry("600x500")
def fetch_url():
    try:
        url_fetched = url.get()
        url_open =urlopen(url_fetched)
        html = url_open.read()
        bs = BeautifulSoup(html, 'lxml')
        t1.insert(1.0, bs.prettify())
    except ValueError:
        messagebox.showwarning('Error', 'Please Input a Valid URL')
    except _tkinter.TclError:
        messagebox.showwarning('Error', 'Please Input a Valid URL')
    except urllib.error.HTTPError:
        messagebox.showinfo('Error','Unable to fetch URL')
def reset():
    e1.delete(0, 'end')
    t1.delete(1.0,END)
l1 = Label(window, text='Enter the url to extract code', pady=10)
l1.grid(row=0, column=1)
url = StringVar()
e1=Entry(window, textvariable=url)
e1.grid(column=1, row=1)
btn1 = Button(window,text='GO',command=fetch_url)
btn1.grid(column=1,row=2)
btn2 = Button(window, text='CLEAR', command=reset)
btn2.grid(column=1, row=3)
t1 = Text(window, pady=10)
t1.grid(row=4, column=1)
window.mainloop()