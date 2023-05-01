from tkinter import *
from tkinter.messagebox import *
from database import *
import os



root = Tk()
root.title("Add bus details")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")

def addbus():
    if(entry1.get()=="" or bus_type.get() == "" or entry3.get() == "" or entry4.get() == "" or entry5.get() == "" or entry6.get() == ""):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        if(entry1.get().isdigit() or entry3.get().isdigit() or entry4.get().isdigit() or entry5.get().isdigit() or entry6.get().isdigit()):
            if(int(entry3.get()) > 70 ):
                showinfo('bus info','seat capacity exceeds 70!!')
            else:

                    show = Label(root,text=f"                                                         ",font="Arial 10 bold")
                    show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
                    curser.execute("select busid from bus")
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
                            editbus()
                        else:
                            pass
                    elif flag == False:
                        id = int(entry1.get())
                        bt = str(bus_type.get())
                        cap = int(entry3.get())
                        fa = int(entry4.get())
                        op = int(entry5.get())
                        ri = int(entry6.get())
                        curser.execute('insert into bus(busid,bustype,capacity,fare,opid,rid) values (?,?,?,?,?,?);' ,(id,bt,cap,fa,op,ri))
                        connect.commit()
                        curser.execute('select * from bus where busid = ?;',(id,))
                        ask = curser.fetchall()
                        # print(ask[0][0])
                        show = Label(root,text=f"{ask[0][0]} {ask[0][1]} {ask[0][2]} {ask[0][3]} {ask[0][4]} {ask[0][5]}",font="Arial 10 bold")
                        show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
                        showinfo("Bus entry","Bus recored added")
                    entry1.delete(0,20)
                    bus_type.set("bus type")
                    entry3.delete(0,20)
                    entry4.delete(0,20)
                    entry5.delete(0,20)
                    entry6.delete(0,20)
        else:
            showinfo('bus info','please add numeric values in appropriate entires!')
            entry1.delete(0,20)
            entry3.delete(0,20)
            entry4.delete(0,20)
            entry5.delete(0,20)
            entry6.delete(0,20)



def editbus():
    if(entry1.get()=="" or bus_type.get() == "" or entry3.get() == "" or entry4.get() == "" or entry5.get() == "" or entry6.get() == ""):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        if(entry1.get().isdigit() or entry3.get().isdigit() or entry4.get().isdigit() or entry5.get().isdigit() or entry6.get().isdigit()):
            if(int(entry3.get()) > 70 ):
                showinfo('bus info','seat capacity exceeds 70!!')
            else:
                show = Label(root,text=f"                          ",font="Arial 10 bold")
                show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
                curser.execute("select busid from bus")
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
                        addbus()
                    else:
                        pass
                elif flag == True:
                    id1 = int(entry1.get())
                    bt1 = str(bus_type.get())
                    cap1 = int(entry3.get())
                    fa1 = int(entry4.get())
                    op1 = int(entry5.get())
                    ri1 = int(entry6.get())
                    # print(bt1)
                    curser.execute('update bus set bustype = ? , capacity= ? , fare = ?, opid = ?, rid = ? where busid = ?;',(bt1,cap1,fa1,op1,ri1,id1))
                    connect.commit()
                    curser.execute('select * from bus where busid = ?;',(id1,))
                    ask1 = curser.fetchall()
                    # print(ask[0][0])
                    show = Label(root,text=f"{ask1[0][0]} {ask1[0][1]} {ask1[0][2]} {ask1[0][3]} {ask1[0][4]} {ask1[0][5]}",font="Arial 10 bold")
                    show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
                    showinfo("Bus entry update","Bus recored updated successfully")
                entry1.delete(0,20)
                bus_type.set("bus type")
                entry3.delete(0,20)
                entry4.delete(0,20)
                entry5.delete(0,20)
                entry6.delete(0,20)
        else:
            showinfo('bus info','please add numeric values in appropriate entires!')
            entry1.delete(0,20)
            entry3.delete(0,20)
            entry4.delete(0,20)
            entry5.delete(0,20)
            entry6.delete(0,20)
        
def home():
    root.destroy()
    os.startfile(".\\frontpage.py")


bus = PhotoImage(file=".\\Bus_for_project.png")
homeimg = PhotoImage(file=".\\home.png")

f1 = Frame(root)
f1.grid(row=0,column=0)
f2  = Frame(root)
f2.grid(row=3,column=0)

Label(f1,image=bus).grid(pady=10,row=0,column=0,padx = (0,0))
Label(f1,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(pady=12,row=1,column=0,padx = (0,0))
Label(f1,text="Add Bus Details",font = "Arial 18 bold",fg="green").grid(pady=12,row=2,column=0,padx = (0,0))



Label(f2,text="Bus id",font="Arial 10 bold").grid(row=3,column=0,padx = (w/6,0))
entry1 = Entry(f2,font="Arial 10 bold")
entry1.grid(row=3,column=1)
Label(f2,text="Bus type",font="Arial 10 bold").grid(row=3,column=2,padx=(0,30))
bus_type = StringVar()
bus_type.set('Bus Type')
option = ['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1']

menu = OptionMenu(f2,bus_type,*option)
menu.grid(row=3,column=3)
Label(f2,text="Capacity",font="Arial 10 bold").grid(row=3,column=4)
entry3 = Entry(f2,font="Arial 10 bold")
entry3.grid(row=3,column=5)

Label(f2,text="Fare Rs",font="Arial 10 bold").grid(row=3,column=6)
entry4 = Entry(f2,font="Arial 10 bold")
entry4.grid(row=3,column=7)

Label(f2,text="Operator ID",font="Arial 10 bold").grid(row=3,column=8)
entry5 = Entry(f2,font="Arial 10 bold")
entry5.grid(row=3,column=9)
Label(f2,text="Route ID",font="Arial 10 bold").grid(row=3,column=10)
entry6 = Entry(f2,font="Arial 10 bold")
entry6.grid(row=3,column=11)

btn1 =Button(f2,text="Add",font="Arial 10 bold",bg="green",command=addbus)
btn1.grid(row=5,column=7,pady=(30,0))
btn2 =Button(f2,text="Edit",font="Arial 10 bold",bg="green",command=editbus)
btn2.grid(row=5,column=8,pady=(30,0))

btn3 = Button(f2,image=homeimg,font="Arial 10 bold",command=home,bg="lightgreen")
btn3.grid(row=5,column=9,pady=(50,0))







root.mainloop()
