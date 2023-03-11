from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('DAILY')
GUI.geometry('700x500')

L1 = Label(GUI,text='❁DAILY❁',font=('supermarket',30),fg='gray')
L1.pack(ipadx=10,ipady=20)

#S1 = Spinbox(font=('supermarket',30),fg='gray')
#S1.pack(ipadx=20,ipady=20)

LB1 = LabelFrame(GUI,text='TO DO LIST')
LB1.pack(ipadx=10,ipady=5)

FB2 = Frame(GUI)
FB2.place(x=100,y=80)

def Button1() :
    formula=str()
    text='You can do it regularly to make your life better :)'
    messagebox.showinfo('Lets do it!',text)

FB1 = Frame(GUI)
FB1.place(x=295,y=220)
B2 = ttk.Button(FB1,text='DO IT!',command=Button1)
B2.pack(ipadx=10,ipady=15)



box1=ttk.Entry(LB1)
box1.grid(row=0,column=0,padx=20,pady=20)

GUI.mainloop()

