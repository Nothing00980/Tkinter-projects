from tkinter import *
from tkinter.messagebox import *
from database import *
import os
root = Tk()
root.title("Route database page")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")

def addroute():
    if(entry1.get()=="" or  entry3.get() == "" or entry2.get() == "" ):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        if(entry1.get().isdigit() and entry3.get().isdigit()):

            show = Label(root,text=f"                                     ",font="Arial 10 bold")
            show.grid(row=4,column=0,columnspan=8,padx = (9*w/40,0))
            curser.execute("select routeid,sid from route")
            data = curser.fetchall()
            flag = False
            for i in data:
                # print(i)
                if i == (int(entry1.get()),int(entry3.get()),):
                    flag = True


                    
            # print(flag)
            if flag == True:
                showerror('DB insertion error',"record already exists...")
                show = Label(root,text=f"                        ",font="Arial 10 bold")
                show.grid(row=4,column=0,columnspan=8,padx = (9*w/40,0))
            elif flag == False:
                id = int(entry1.get())
                sname = str(entry2.get())
                sid = int(entry3.get())
            
                curser.execute('insert into route(routeid,sid,sname) values(?,?,?);' ,(id,sid,sname))
                connect.commit()
                curser.execute('select * from route where routeid = ? and sid = ?;',(id,sid))
                ask = curser.fetchall()
                # print(ask[0][0])
                show = Label(root,text=f"{ask[0][0]} {ask[0][1]} {ask[0][2]}",font="Arial 10 bold")
                show.grid(row=4,column=0,columnspan=8,padx = (9*w/40,0))
                showinfo("route entry","route recored added")
            entry1.delete(0,20)
            entry2.delete(0,20)
            entry3.delete(0,20)
        else:
            showinfo('bus info','please add numeric values in appropriate entires!')
            entry1.delete(0,20)
            entry3.delete(0,20)

def deleteroute():
    if(entry1.get()=="" or  entry3.get() == "" or entry2.get() == "" ):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        if(entry1.get().isdigit() and entry3.get().isdigit()):

            show = Label(root,text=f"                                ",font="Arial 10 bold")
            show.grid(row=4,column=0,columnspan=12,padx = (9*w/40,0))
            curser.execute("select routeid,sid from route")
            data = curser.fetchall()
            # print(data)
            flag = False
            for i in data:
                # print(i)
                if i == (int(entry1.get()),int(entry3.get(),)):
                    flag = True


                    
            # print(flag)
            if flag == False:
                showerror('DB deletion error',"record doesnt exists!!...")
                up = askyesno("data add","record doesn't exist do you want to add  it ?")
                if up == YES:
                    addroute()
                else:
                    pass
            elif flag == True:
                id = int(entry1.get())
                sname = str(entry2.get())
                sid = int(entry3.get())
                # print(bt1)
                curser.execute('delete from route where routeid = ? and sid= ? ;',(id,sid))
                connect.commit()

                showinfo("route entry delete","route recored deleted successfully")
            entry1.delete(0,20)
            entry2.delete(0,20)
            entry3.delete(0,20)
        else:
            showinfo('bus info','please add numeric values in appropriate entires!')
            entry1.delete(0,20)
            entry3.delete(0,20)

    
def home():
    root.destroy()
    os.startfile(".\\frontpage.py")


bus = PhotoImage(file=".\\Bus_for_project.png")
homeimg = PhotoImage(file=".\\home.png")

Label(root,image=bus).grid(pady=10,row=0,column=0,columnspan=8,padx = (w/3,0))
Label(root,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(pady=12,row=1,column=0,columnspan=8,padx = (w/3,0))
Label(root,text="Add Bus Route Details",font = "Arial 18 bold",fg="green").grid(pady=12,row=2,column=0,columnspan=8,padx = (w/3,0))



Label(root,text="Route ID",font="Arial 10 bold").grid(row=3,column=0,padx = (9*w/40,0))
entry1 = Entry(root,font="Arial 10 bold")
entry1.grid(row=3,column=1)
Label(root,text="Station Name",font="Arial 10 bold").grid(row=3,column=2,padx=(0,30))

entry2 = Entry(root,font="Arial 10 bold")
entry2.grid(row=3,column=3)
Label(root,text="Station ID",font="Arial 10 bold").grid(row=3,column=4)
entry3 = Entry(root,font="Arial 10 bold")
entry3.grid(row=3,column=5)



btn1 =Button(root,text="Add Route",font="Arial 10 bold",bg="green",command=addroute)
btn1.grid(row=3,column=6)
btn2 =Button(root,text="Delete Route",font="Arial 10 bold",bg="green",fg='red',command=deleteroute)
btn2.grid(row=3,column=7)

btn3 = Button(root,image=homeimg,font="Arial 10 bold",command=home,bg="lightgreen")
btn3.grid(row=5,column=5,pady=(50,0))







root.mainloop()
