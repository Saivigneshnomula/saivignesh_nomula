#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nomul
#
# Created:     19-02-2024
# Copyright:   (c) nomul 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
root=Tk()
root.geometry("500x300")

def submit_value():
    print("your information has been saved successfully")

Label(root,text="Student Registration Form",font="times 15 bold").grid(row=0,column=3)

name_stu=Label(root,text="Student Name")
name_stu.grid(row=1,column=2)
branch_stu=Label(root,text="Branch")
branch_stu.grid(row=2,column=2)


name_value=StringVar
branch_value=StringVar
check_value=IntVar


name_box=Entry(root,textvariable=name_value)
name_box.grid(row=1,column=3)
branch_box=Entry(root,textvariable=branch_value)
branch_box.grid(row=2,column=3)

check_box=Checkbutton(text="Add or not??",variable=check_value)
check_box.grid(row=3,column=3)

Button(text="Submit",command=submit_value).grid(row=4,column=3)
root.mainloop()
