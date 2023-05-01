from tkinter import *
from turtle import undo
from unittest import main
# from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("untitled - notepad ")
    file = None
    textarea.delete(1.0,END)
def newwindow():
    pass
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes = [("All Files","*.*"),("text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - notepad")
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile= 'untitled.txt',defaultextension=".txt",filetypes = [("All Files","*.*"),("text Documents","*.txt")])
        if file == "":
            file = None
        else:
            # save as a new file
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - notepad")

    else:
        f = open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
def saveasfile():
    pass
def exit():
    root.destroy()
def undo():
    pass
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def delete():
    pass
def aboutnotepad():
    showinfo("NOTEPAD","note pad by yuvraj bhati")
    

if __name__ == '__main__':

    root = Tk()
    root.geometry("800x800")
    root.title("my notepad")
    # image = Image.open("iconnotepad.ico")
    # photo = ImageTk.PhotoImage(image)
    # root.wm_iconbitmap(photo)



    scrollbary = Scrollbar(root)
    scrollbary.pack(side = RIGHT,fill=Y)
    scrollbarx = Scrollbar(root,orient=HORIZONTAL)
    scrollbarx.pack(side = BOTTOM,fill=X)
    textarea = Text(root,font = "lucidia 12",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    textarea.pack(expand = True ,fill=BOTH)

    scrollbary.config(command = textarea.yview)
    scrollbarx.config(command = textarea.xview)

    file = None

    menu = Menu(root)
    filemenu = Menu(menu,tearoff=0)
    filemenu.add_command(label="NEW",command=newfile)
    filemenu.add_command(label="NEW WINDOW",command=newwindow)
    filemenu.add_command(label="OPEN",command=openfile)
    filemenu.add_command(label="SAVE",command=savefile)
    filemenu.add_command(label="SAVE AS",command=saveasfile)
    filemenu.add_separator()
    filemenu.add_command(label="PAGE SETUP",command=newfile)
    filemenu.add_command(label="PRINT",command=newfile)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT",command=exit)
    menu.add_cascade(label="FILE",menu = filemenu)

    editmenu = Menu(menu,tearoff=0)
    editmenu.add_command(label="UNDO",command = undo)
    editmenu.add_separator()
    editmenu.add_command(label="CUT",command = cut)
    editmenu.add_command(label="COPY",command = copy)
    editmenu.add_command(label="PASTE",command = paste)
    editmenu.add_command(label="DELETE",command = delete)
    editmenu.add_separator()
    editmenu.add_command(label="SEARCH WITH BING",command = newfile)
    editmenu.add_command(label="FIND",command = newfile)
    editmenu.add_command(label="FIND NEXT ",command = newfile)
    editmenu.add_command(label="FIND PREVIOUS",command = newfile)
    editmenu.add_command(label="REPLACE",command = newfile)
    editmenu.add_command(label="GO TO",command = newfile)
    editmenu.add_separator()
    editmenu.add_command(label="SELCET ALL",command = newfile)
    editmenu.add_command(label="TIME/DATE",command = newfile)
    menu.add_cascade(label="EDIT",menu = editmenu)

    formatmenu = Menu(menu,tearoff=0)
    formatmenu.add_command(label="word wrap",command = format)
    formatmenu.add_command(label="font...",command = format)
    menu.add_cascade(label="FORMAT",menu = formatmenu)

    view = Menu(menu,tearoff=0)
    zoom = Menu(view,tearoff=0)
    view.add_cascade(label="ZOOM",menu = zoom)
    zoom.add_command(label="ZOOM IN")
    zoom.add_command(label="ZOOM OUT")
    zoom.add_command(label="RESTORE DEFAULT ZOOM")


    view.add_command(label="STATUS BAR",command=format)
    menu.add_cascade(label = "VIEW",menu = view)

    help = Menu(menu,tearoff=0)
    help.add_command(label="view help")
    help.add_command(label="send feedback")
    help.add_separator()
    help.add_command(label="about notepad",command=aboutnotepad)
    menu.add_cascade(label="HELP",menu = help)






    root.config(menu = menu)


    root.mainloop()
