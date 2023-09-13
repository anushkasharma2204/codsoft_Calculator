from tkinter import*
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnclear():
    global val
    val=""
    data.set("")
def btnequals():
    global val
    result=str(eval(val))
    data.set(result)
root=Tk()
root.title("MY CALCULATOR")
root.geometry("360x321+400+170")
val=""
data=StringVar()
display=Entry(root,textvariable=data,bd=22,justify=RIGHT,bg="sky blue",font=("ariel",20))
display.grid(row=0,columnspan=4)
Btn7=Button(root,text="7",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(7))
Btn7.grid(row=1,column=0)
Btn8=Button(root,text="8",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(8))
Btn8.grid(row=1,column=1)
Btn9=Button(root,text="9",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(9))
Btn9.grid(row=1,column=2)
Btn_add=Button(root,text="+",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick('+'))
Btn_add.grid(row=1,column=3)
Btn4=Button(root,text="4",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(4))
Btn4.grid(row=2,column=0)
Btn5=Button(root,text="5",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(5))
Btn5.grid(row=2,column=1)
Btn6=Button(root,text="6",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(6))
Btn6.grid(row=2,column=2)
Btn_sub= Button(root,text="-",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick('-'))
Btn_sub.grid(row=2,column=3)
Btn1=Button(root,text="1",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(1))
Btn1.grid(row=3,column=0)
Btn2=Button(root,text="2",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(2))
Btn2.grid(row=3,column=1)
Btn3=Button(root,text="3",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(3))
Btn3.grid(row=3,column=2)
Btn_div=Button(root,text="*",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick('*'))
Btn_div.grid(row=3,column=3)
Btn_c=Button(root,text="C",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=btnclear)
Btn_c.grid(row=4,column=0)
Btn0=Button(root,text="0",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick(0))
Btn0.grid(row=4,column=1)
Btn_div=Button(root,text="/",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=lambda:btnclick('/'))
Btn_div.grid(row=4,column=2)
Btn_eq=Button(root,text="=",font=("ariel",12,"bold"),bd=12,height=1,width=4,command=btnequals)
Btn_eq.grid(row=4,column=3)

root.mainloop()