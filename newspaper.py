from textwrap import fill
from tkinter import *
from PIL import Image,ImageTk

def every_100(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text+= text[i]
        if i%100==0  and i!=0:
            final_text+="\n"
    return final_text
root = Tk()
root.title("times of india--by yuvraj bhati")
root.geometry("1000x800")
texts = []
photos = []
for i in range(0,2):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.jpg")
    # TODO: resize this image
    image = image.resize((225,265),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width = 800,height = 70,bg = "black")
Label(f0,text = "News by yuvraj bhati",font = "lucidia 33 bold").pack()
Label(f0,text = "march 7,2022",font = "lucidia 13 bold").pack()
f0.pack()

f1 = Frame(root,width = 900,height = 200,pady = 34,padx = 22)
Label(f1,text = texts[0]).pack(side = "left")
Label(f1,image = photos[0],anchor = "e",fg = "white").pack()
f1.pack(anchor = "w",fill=X)


f2 = Frame(root,width = 900,height = 200,pady = 34,padx = 22)
Label(f2,text = texts[1]).pack(side = "right")
Label(f2,image = photos[1],anchor = "e").pack()
f2.pack(anchor = "w",fill=X)


root.mainloop()