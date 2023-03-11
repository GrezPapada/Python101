from tkinter import *
from tkinter import ttk #theme of tk 
from tkinter import messagebox

GUI = Tk()#T ต้องเป็นตัวใหญ่เท่านั้น
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400')# geometry ขนาดของหน้าจอโปรแกรม

#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท') #ปุ่ม
#B1.pack(ipadx=20,ipady=20)#.pack ทำให้ปุ่มอยู๋ด้านบนกลางหน้าจอ
L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
###########################################
def Button2() :
    text = 'ตอนนี้มีเงินในบัญชีอยู๋ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    #showinfo
    #showwarning
    #showerror
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)#command ผูกfuntion
B2.pack(ipadx=20,ipady=20)
###########################################
def Button3() :
    text = 'Python 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)#titlemessagebox
    #showinfo
    #showwarning
    #showerror
FB2 = Frame(GUI)
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button3)#command ผูกfuntion
B3.pack(ipadx=20,ipady=20)

#FB1 = LabelFrame(GUI,text=''Money)#titleLabel
#FB1.place(x=100,y=300)
#B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
#B2.pack(ipadx=20,ipady=20,padx=30,pady=30)#กรอบของbutton

GUI.mainloop()
