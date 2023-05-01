from tkinter import *
from tkinter.messagebox import *
from database import *
import os

root = Tk()
root.title("bus operator details")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")

def add():
    if(entry1.get()==""  or entry3.get() == "" or entry4.get() == "" or entry5.get() == "" ):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        if(entry1.get().isdigit() and entry4.get().isdigit()):


            show = Label(root,text=f"                                    ",font="Arial 10 bold")
            show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
            curser.execute("select operatorid from operator")
            data = curser.fetchall()
            flag = False
            for i in data:
                # print(i)
                if i == (int(entry1.get()),):
                    flag = True


                    
            # print(flag)
            if flag == True:
                showerror('DB insertion error',"record already exists...")
                up = askyesno("data upadte","record already exist do you want to update it ?")
                if up == YES:
                    edit()
                else:
                    show = Label(root,text=f"                                    ",font="Arial 10 bold")
                    show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
                    
            elif flag == False:
                id = int(entry1.get())
                name = str(entry2.get())
                ad = str(entry3.get())
                phone = str(entry4.get())
                email = str(entry5.get())
                curser.execute('insert into operator(operatorid,op_name,address,phonenumber,email) values (?,?,?,?,?);' ,(id,name,ad,phone,email))
                connect.commit()
                curser.execute('select * from operator where operatorid = ?;',(id,))
                ask = curser.fetchall()
                # print(ask[0][0])
                show = Label(root,text=f"{ask[0][0]} {ask[0][1]} {ask[0][2]} {ask[0][3]} {ask[0][4]}",font="Arial 10 bold")
                show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
                showinfo("operator entry","operator recored added")
            entry1.delete(0,20)
            entry2.delete(0,20)
            entry3.delete(0,20)
            entry4.delete(0,20)
            entry5.delete(0,20)
        else:
            showinfo('bus info','please add numeric values in appropriate entires!')
            entry1.delete(0,20)
            entry4.delete(0,20)



 
def edit():
    if(entry1.get()=="" or entry3.get() == "" or entry4.get() == "" or entry5.get() == "" ):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        if(entry1.get().isdigit() and entry4.get().isdigit()):



            show = Label(root,text=f"                         ",font="Arial 10 bold")
            show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
            curser.execute("select operatorid from operator")
            data = curser.fetchall()
            flag = False
            for i in data:
                # print(i)
                if i == (int(entry1.get()),):
                    flag = True


                    
            # print(flag)
            if flag == False:
                showerror('DB updation error',"record doesnt exists!!...")
                up = askyesno("data add","record doesn't exist do you want to add  it ?")
                if up == YES:
                    add()
                else:
                    pass
            elif flag == True:
                id = int(entry1.get())
                name = str(entry2.get())
                ad = str(entry3.get())
                phone = str(entry4.get())
                email = str(entry5.get())
                # print(bt1)
                curser.execute('update operator set op_name = ? , address= ? , phonenumber = ?, email = ? where operatorid = ?;',(name,ad,phone,email,id))
                connect.commit()
                curser.execute('select * from operator where operatorid = ?;',(id,))
                ask1 = curser.fetchall()
                # print(ask[0][0])
                show = Label(root,text=f"{ask1[0][0]} {ask1[0][1]} {ask1[0][2]} {ask1[0][3]} {ask1[0][4]}",font="Arial 10 bold")
                show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
                showinfo("operator entry update","operator recored updated successfully")
            entry1.delete(0,20)
            entry2.delete(0,20)
            entry3.delete(0,20)
            entry4.delete(0,20)
            entry5.delete(0,20)
        else:
            showinfo('bus info','please add numeric values in appropriate entires!')
            entry1.delete(0,20)
            entry4.delete(0,20)
def home():
    root.destroy()
    os.startfile(".\\frontpage.py")


bus = PhotoImage(file=".\\Bus_for_project.png")
homeimg = PhotoImage(file=".\\home.png")

Label(root,image=bus).grid(pady=10,row=0,column=0,columnspan=12,padx = (w/5,0))
Label(root,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(pady=12,row=1,column=0,columnspan=12,padx = (w/5,0))
Label(root,text="Add Bus Operator Details",font = "Arial 16 bold",fg = "green").grid(pady=12,row=2,column=0,columnspan=12,padx = (w/5,0))
Label(root,text="operator id",font="Arial 10 bold").grid(row=3,column=0,padx = (9*w/40,0))
entry1 = Entry(root,font="Arial 10 bold")
entry1.grid(row=3,column=1)
Label(root,text="Name",font="Arial 10 bold").grid(row=3,column=2,padx=(0,30))
entry2 = Entry(root,font="Arial 10 bold")
entry2.grid(row=3,column=3)
Label(root,text="Address",font="Arial 10 bold").grid(row=3,column=4)
entry3 = Entry(root,font="Arial 10 bold")
entry3.grid(row=3,column=5)

Label(root,text="Phone",font="Arial 10 bold").grid(row=3,column=6)
entry4 = Entry(root,font="Arial 10 bold")
entry4.grid(row=3,column=7)

Label(root,text="Email",font="Arial 10 bold").grid(row=3,column=8)
entry5 = Entry(root,font="Arial 10 bold")
entry5.grid(row=3,column=9)

btn1 =Button(root,text="Add",font="Arial 10 bold",bg="green",command=add)
btn1.grid(row=3,column=10)
btn2 =Button(root,text="Edit",font="Arial 10 bold",bg="green",command=edit)
btn2.grid(row=3,column=11)

btn3 = Button(root,image=homeimg,font="Arial 10 bold",command=home,bg="lightgreen")
btn3.grid(row=5,column=9,pady=(50,0))
