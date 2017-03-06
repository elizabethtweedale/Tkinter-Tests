from tkinter import *

skyWide, skyHigh = 1, 1

def newTower():
    global skyWide, skyHigh
    skyWide = varW.get()
    skyHigh = varH.get()
    myBuilding.delete("all")
    for i in range(skyWide):
        for j in range(skyHigh):
            # create_rectangle(startX(left), startY(top), finishX(right), finishY(bottom), outline, fill)
            myBuilding.create_rectangle((15*i+10),(15*j+10),(15*i+20),(15*j+20),outline="#fb7",fill=None)
    myBuilding.pack(fill=BOTH, expand=1)
    

root = Tk()
myBuilding = Canvas(root, width=500, height=500)
root.title("Skyscraper")
myBuilding.pack()

varW = IntVar()
scaleW = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varW, label="Windows Wide")
scaleW.pack()

varH = IntVar()
scaleH = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varH, label="Windows High")
scaleH.pack()

button1 = Button(root, text="Draw Windows", command=newTower)
button1.pack()

root.mainloop()
