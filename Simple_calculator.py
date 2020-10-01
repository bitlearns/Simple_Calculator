#Before this correction there was 100+ problem but all problems are solved now.




#Here i am importing tk,Button etc individually 
from tkinter import Tk
from tkinter import Button
from tkinter import END
from tkinter import Entry 

root=Tk()
root.title("Simple Calculator")

#Creating Entry box In Top
 
e=Entry(root,width=35,borderwidth=5) 
e.grid(row=0 , column=0 , columnspan=5 ,padx=10 , pady=10)

#Defining the Functions
#Here we are defining c as e.delete so that any written no. can be delecte when we click on c button.
def button_click(number):
    c=e.get()
    e.delete(0 , END)
    e.insert(0,str(c)+str(number))

def button_clear():
    e.delete(0 , END)

def  button_add():
    first_num=e.get()
    global f_num 
    global func 
    func="addition"
    f_num=float(first_num)
    e.delete(0, END)

def button_sub():
    first_num=e.get()
    global f_num 
    global func 
    func="subtraction"
    f_num=float(first_num)
    e.delete(0, END)

def button_mul():
    first_num=e.get()
    global f_num 
    global func 
    func="multiplication"
    f_num=float(first_num)
    e.delete(0, END)

def button_div():
    first_num=e.get()
    global f_num 
    global func 
    func="division"
    f_num=float(first_num)
    e.delete(0, END)

def button_equal():
    second_num=e.get()
    e.delete(0, END)
    if func=="addition":
        e.insert(0,f_num + int(second_num))
    elif func=="subtraction":
        e.insert(0,f_num - int(second_num))
    elif func=="multiplication":
        e.insert(0,f_num * int(second_num))
    elif func=="division":
        e.insert(0,f_num / int(second_num))

def button_info():
    print("Made By Aswin")

#Creating buttons for usage
b1=Button(root,text="1",padx=40,pady=20,command=lambda : button_click(1))
b2=Button(root,text="2",padx=40,pady=20,command=lambda : button_click(2))
b3=Button(root,text="3",padx=40,pady=20,command=lambda : button_click(3))
b4=Button(root,text="4",padx=40,pady=20,command=lambda : button_click(4))
b5=Button(root,text="5",padx=40,pady=20,command=lambda : button_click(5))
b6=Button(root,text="6",padx=40,pady=20,command=lambda : button_click(6))
b7=Button(root,text="7",padx=40,pady=20,command=lambda : button_click(7))
b8=Button(root,text="8",padx=40,pady=20,command=lambda : button_click(8))
b9=Button(root,text="9",padx=40,pady=20,command=lambda : button_click(9))
b0=Button(root,text="0",padx=40,pady=20,command=lambda : button_click(0))
bi=Button(root,text="!",padx=40,pady=10,command=button_info)
b_add=Button(root,text="+",padx=38,pady=20,command=button_add)
b_sub=Button(root,text="-",padx=41,pady=20,command=button_sub)
b_mul=Button(root,text="*",padx=40,pady=20,command=button_mul)
b_div=Button(root,text="/",padx=41,pady=20,command=button_div)
b_clear=Button(root,text="c",padx=40,pady=20,command=button_clear)
b_equal=Button(root,text="=",padx=38,pady=20,command=button_equal)

#showing buttons on screen

b1.grid(row=3 , column= 0)
b2.grid(row=3 , column= 1)
b3.grid(row=3 , column= 2)

b4.grid(row=2 , column=0 )
b5.grid(row=2 , column=1 )
b6.grid(row=2 , column=2 )

b7.grid(row=1 , column=0 )
b8.grid(row=1 , column=1 )
b9.grid(row=1 , column=2 )

b0.grid(row=4 , column=0 )
b_add.grid(row=1 , column=5 )
b_clear.grid(row=4 , column=1)
b_equal.grid(row=4 , column=2)

b_sub.grid(row=2 ,column=5)
b_mul.grid(row=3 ,column=5)
b_div.grid(row=4 ,column=5)

bi.grid(row=0 , column = 5)

root.mainloop()


#Now this code has 0 problem 
#UtkarshVerma
